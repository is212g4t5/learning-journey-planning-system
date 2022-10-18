<template>
  <q-page class="">

    <q-breadcrumbs class="q-ml-md q-mt-md">
      <template v-slot:separator>
        <q-icon
          size="1.5em"
          name="chevron_right"
          color="primary"
        />
      </template>
      <q-breadcrumbs-el to="/HR" >HR Management</q-breadcrumbs-el>
      <q-breadcrumbs-el>{{tab}}</q-breadcrumbs-el>
    </q-breadcrumbs>

    <div class="text-center font-700" style="color:#525252; font-size:28px">HR Management</div>
    <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:75px;height:2px"></div>

    <q-tabs
        v-model="tab"
        align="justify"
        narrow-indicator
        class="text-grey-9" 
        active-class="text-primary"
        style="border-bottom:1px solid grey"
      >
        <q-tab class="" name="View Job Roles" label="View Job Roles" no-caps />
        <q-tab class="" name="View Skills" label="View Skills" no-caps />
        <q-tab class="" name="View Courses" label="View Courses" no-caps/>
      </q-tabs>

      <q-tab-panels
          v-model="tab"
          animated
          transition-prev="fade"
          transition-next="fade"
          class=""
        >
        <!-- job roles panel -->
          <q-tab-panel name="View Job Roles" >
            <q-btn label="Add New Role" color="primary" no-caps class="addButton absolute" style="right:30px; top:30px;z-index:1" @click="addJobDialog = !addJobDialog"></q-btn>
            
            <div class="text-center" v-if="jobsEmpty">
              <Lottie :options="defaultOptions" style="width:20vw" />
              <div class="font-700 font-size-28">No Roles Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>

            <q-table
            v-else
            title="Job Roles"
            :data="jobData"
            :columns="jobColumns"
            row-key="name"
            :rows-per-page-options="[10]"
          >
            <template v-slot:body="props">
              <q-tr :props="props">
                <q-td key="id" :props="props">
                  {{ props.row.id }}
                </q-td>
                <q-td key="name" :props="props">
                    {{ props.row.name }}
                </q-td>
                <q-td key="description" :props="props">
                    {{ props.row.description }}
                </q-td>
                <q-td key="skills" :props="props">
                  <q-badge v-for="(skill,index) in props.row.skills" :key="index" v-if="skill.active==true" color="orange" class="q-mr-xs">
                    {{skill.name}}
                  </q-badge>
                </q-td>
                <q-td key="status" :props="props">
                  <q-badge v-if="props.row.active == true" color="green" class="q-mr-xs">
                    Active
                  </q-badge>
                  <q-badge v-else color="red" class="q-mr-xs">
                    Inactive
                  </q-badge>
                </q-td>

                <q-td key="buttons" :props="props" class="q-gutter-x-sm">
                    <q-btn label="Edit" color="orange" outline no-caps @click="openEditJobPopup(props.row)"></q-btn>
                    <q-btn label="Assign Skills" color="green" outline no-caps @click="openAssignPopup(props.row)"></q-btn>
                    <q-btn label="Remove" color="red" outline no-caps @click="deleteJob(props.row)"></q-btn>
                </q-td>
                
              </q-tr>
            </template>
          </q-table>
          </q-tab-panel>

          <!-- skills panel -->
          <q-tab-panel name="View Skills" >
            <q-btn label="Add New Skill" color="primary" no-caps class="addButton absolute" style="right:30px; top:30px;z-index:1" @click="addSkillDialog = !addSkillDialog"></q-btn>
            <div class="text-center" v-if="skillsEmpty">
              <Lottie :options="defaultOptions"  style="width:20vw" />
              <div class="font-700 font-size-28">No Skills Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>


            <q-table
            v-else
            title="Skills"
            :data="skillData"
            :columns="skillColumns"
            row-key="name"
            :rows-per-page-options="[10]"
          >
            <template v-slot:body="props">
              <q-tr :props="props">
                <q-td key="id" :props="props">
                  {{ props.row.id }}
                </q-td>
                <q-td key="name" :props="props">
                    {{ props.row.name }}
                </q-td>
                <q-td key="description" :props="props">
                    {{ props.row.description }}
                </q-td>
                <q-td key="status" :props="props">
                  <q-badge v-if="props.row.active == true" color="green" class="q-mr-xs">
                    Active
                  </q-badge>
                  <q-badge v-else color="red" class="q-mr-xs">
                    Inactive
                  </q-badge>
                </q-td>

                <q-td key="buttons" :props="props" class="q-gutter-x-sm">
                    <q-btn label="Edit" color="orange" outline no-caps @click="openEditSkillPopup(props.row)"></q-btn>
                    <q-btn v-if="props.row.active==true" label="Remove" color="red" outline no-caps @click="deleteSkill(props.row)"></q-btn>
                </q-td>
                
              </q-tr>

            </template>
          </q-table>

          </q-tab-panel>


          <!-- courses panel -->
          <q-tab-panel name="View Courses" v-show="coursesEmpty">
            
            <div class="text-center" v-if="coursesEmpty">
              <Lottie :options="defaultOptions"  style="width:20vw" />
              <div class="font-700 font-size-28">No Courses Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>


            




          </q-tab-panel>
        </q-tab-panels>
    
        
        <!-- add job dialog -->
        <q-dialog v-model="addJobDialog">
          <q-card class="q-pa-md" style="width:50vw">
            <div class="text-center font-700" style="color:#525252; font-size:28px">Add Job Role</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

            <form @submit.prevent.stop="onJobSubmit" >
              <div class="q-mx-md">
                <div class="font-size-16 q-mb-xs">Job Role Name</div>
                <q-input ref="jobRoleName" outlined v-model="jobRoleName" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Job Role Name" style="font-size:16px" />
              </div>

              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">Job Role Description</div>
                <q-input ref="jobRoleDescription" type="textarea" outlined v-model="jobRoleDescription" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Job Role Description" style="font-size:16px" />
              </div>
           
            

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Add Job" color="primary" type="submit" />
            </q-card-actions>

            </form>
          </q-card>
        </q-dialog>

        <!-- edit job dialog -->
        <q-dialog v-model="editJobDialog">
          <q-card class="q-pa-md" style="width:50vw">
            <div class="text-center font-700" style="color:#525252; font-size:28px">Edit Job Role</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

            <form @submit.prevent.stop="onEditJobRole" >
              <div class="q-mx-md">
                <div class="font-size-16 q-mb-xs">Job Role Name</div>
                <q-input ref="editJobRoleName" outlined v-model="editJobRoleName" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Job Role Name" style="font-size:16px" />
              </div>

              <div class="q-mx-md">
                <div class="font-size-16 q-mb-xs">Job Role Description</div>
                <q-input ref="editJobRoleDescription" type="textarea" outlined v-model="editJobRoleDescription" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Job Role Description" style="font-size:16px" />


                <div class="font-size-16 q-mb-xs ">Skill Status</div>
                <q-select
                class=""
                outlined
                v-model="editJobStatusOption"
                :options="['Active','Inactive']"
                :rules="[val => !!val || 'Field is required']"
                style="font-size:16px"
              />
              </div>
           
            

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Edit" color="primary" type="submit" />
            </q-card-actions>

            </form>
          </q-card>
        </q-dialog>

        <!-- assign skill to job dialog -->
        <q-dialog v-model="assignDialog">
          <q-card class="q-pa-md" style="width:50vw">
            <div class="text-center font-700" style="color:#525252; font-size:28px">Assign Skill To Job Role</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

            <form @submit.prevent.stop="onAssignSkillToJobRole" >
              <div class="q-mx-md">
                <div class="font-size-16 q-mb-xs">Job Role Name</div>
                <q-input ref="assignJobRoleName" outlined v-model="assignJobRoleName" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Job Role Name" style="font-size:16px" disable />
              </div>

              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">Job Role Description</div>
                <q-input ref="assignJobRoleDescription" type="textarea" outlined v-model="assignJobRoleDescription" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Job Role Description" style="font-size:16px" disable />
              </div>

              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Select Skills</div>
                <q-select
                
                autofocus
                filled
                v-model="skillOptions"
                multiple
                :options="skillOptionsArray"
                :rules="[val => !!val || 'Field is required']"
                style="font-size:16px"
              />
              </div>
             
           
            

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Assign" color="primary" type="submit" />
            </q-card-actions>

            </form>
          </q-card>
        </q-dialog>


        <!-- add skill dialog -->
        <q-dialog v-model="addSkillDialog">
          <q-card class="q-pa-md" style="width:50vw">
            <div class="text-center font-700" style="color:#525252; font-size:28px">Add Skill</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

            <form @submit.prevent.stop="onSkillSubmit" >
              <div class="q-mx-md">
                <div class="font-size-16 q-mb-xs">Skill Title</div>
                <q-input ref="skillName" outlined v-model="skillName" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Skill Name" style="font-size:16px" />
              </div>

              <div class="q-mx-md q-mt-md">
                <div class="font-size-16 q-mb-xs">Skill Description</div>
                <q-input ref="skillDescription" type="textarea" outlined v-model="skillDescription" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Skill Description" style="font-size:16px" />
              </div>
           
            

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Add Skill" color="primary" type="submit" />
            </q-card-actions>

            </form>
          </q-card>
        </q-dialog>


        <!-- edit skill dialog -->
        <q-dialog v-model="editSkillDialog">
          <q-card class="q-pa-md" style="width:50vw">
            <div class="text-center font-700" style="color:#525252; font-size:26px">Edit Skill</div>
            <div class="q-mx-auto " style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

            <form @submit.prevent.stop="onEditSkill" >
              <div class="q-mx-md">
                <div class="font-size-16 q-mb-xs">Skill Name</div>
                <q-input ref="editSkillName" outlined v-model="editSkillName" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Skill Name" style="font-size:16px" />
              </div>

              <div class="q-mx-md ">
                <div class="font-size-16 q-mb-xs">Skill Description</div>
                <q-input ref="editSkillDescription" type="textarea" outlined v-model="editSkillDescription" :rules="[val => !!val || 'Field is required']" class="" placeholder="Enter a Skill Description" style="font-size:16px" />
                
                  <div class="font-size-16 q-mb-xs q-mt-md">Skill Status</div>
                <q-select
                class=""
                outlined
                v-model="editSkillStatusOption"
                :options="['Active','Inactive']"
                :rules="[val => !!val || 'Field is required']"
                style="font-size:16px"
              />
              </div>
           
              

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Edit" color="primary" type="submit" />
            </q-card-actions>

            </form>
          </q-card>
        </q-dialog>
    
  </q-page>
</template>

<script>
import Lottie from 'vue-lottie';
import * as animationData from './empty.json';
import axios from 'axios'
export default {
  methods: {
    async onJobSubmit () {
      this.$refs.jobRoleName.validate()
      this.$refs.jobRoleDescription.validate()

      if (this.$refs.jobRoleName.hasError || this.$refs.jobRoleDescription.hasError) {
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Inputs cannot be empty'
        })
      }
      else {

        // // add else if the name already inside database, throw error
        let nameExists = false
        this.jobData.forEach(element => {
          if (this.jobRoleName == element.name){
            nameExists = true
            return
          }
        });

        if (nameExists == true){
          this.$q.notify({
            color: 'negative',
            icon:'error',
            message: `Job role: '${this.jobRoleName}'' already inside database`
          })
        }else{
          let postRes = await axios.post('http://127.0.0.1:5000/api/roles/',{
            name:this.jobRoleName,
            description:this.jobRoleDescription,
            active:true 
          }).catch(err=>{
            console.log('STATUS CODE',err.stats)
            this.$q.notify({
              color: 'negative',
              icon:'error',
              message: 'Failed to add to database'
            })
            return
          })

          // refresh table again
          this.getJobTable()
          
          this.addJobDialog = false
          
          this.$q.notify({
            icon: 'done',
            color: 'positive',
            icon:'done',
            message: 'Submitted'
          })
        }

        // reset every enter
        this.jobRoleName=''
        this.jobRoleDescription=''

       

       
      }

   
    },
    async getJobTable(){
      let roleData = await axios.get('http://127.0.0.1:5000/api/roles/skills')
      this.jobsEmpty = true

      let currJobData = []

      roleData.data.forEach(element => {
        // if (element.active == true){
        //   this.jobsEmpty = false
        //   currJobData.push(element)
          
        // }
        this.jobsEmpty = false
        currJobData.push(element)
      });

      
      this.jobData = currJobData
      console.log('job data:',this.jobData)
    },

    async openEditJobPopup(row){
      this.editJobDialog = true
      this.editJobRoleName = row.name
      this.editJobRoleDescription = row.description
      this.editRowId = row.id

      console.log(row)
      this.editJobStatusOption = row.active
      if (row.active == true){
        this.editJobStatusOption = 'Active'
      }else{
        this.editJobStatusOption = 'Inactive'
      }
    },
    async onEditJobRole(){
      //basically same as onSubmit but instead of POST is PUT
      this.$refs.editJobRoleName.validate()
      this.$refs.editJobRoleDescription.validate()

      if (this.$refs.editJobRoleName.hasError || this.$refs.editJobRoleDescription.hasError) {
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Inputs cannot be empty'
        })
      }
      else {

        let jobStatus = ''
        if (this.editJobStatusOption == 'Active'){
          jobStatus = true
        }else{
          jobStatus = false
        }

        let editPass = true
          let updateRes = await axios.put(`http://127.0.0.1:5000/api/roles/${this.editRowId}`,{
            name:this.editJobRoleName,
            description:this.editJobRoleDescription,
            active:jobStatus
          }).catch(err=>{
            console.log(err)
            this.$q.notify({
              color: 'negative',
              icon:'error',
              message: 'Failed to update row in database'
            })
            editPass = false
            return
          })

          // refresh table again
          this.getJobTable()
          
          
          this.editJobDialog = false
          

          if (editPass == true){
            this.$q.notify({
              icon: 'done',
              color: 'positive',
              icon:'done',
              message: 'Edited role'
            })
          }
          
        }

        // reset every enter
        this.editJobRoleName=''
        this.editJobRoleDescription=''

    
    },

    
    openAssignPopup(row){
      console.log(row)

      //open dialog, store all the disabled fields
      this.assignDialog = true
      this.assignJobRoleName = row.name
      this.assignJobRoleDescription = row.description
      this.assignRowId = row.id

      console.log('ASSIGN ROLE ID', this.assignRowId)

      //store all skills as options 
      let skillsArray = []
      this.skillData.forEach(element => {
        if (element.active == true){
          skillsArray.push(element.name)
        }
        
      });
      this.skillOptionsArray = skillsArray



      let skillsOptionsSelected = []
      this.jobData.forEach(element => {
        if (element.id == row.id){
          console.log('ELEMENT SKILLS OPTIONS SELECTED', element)
          element.skills.forEach(indivSkill => {
            if (indivSkill.active == true){
              skillsOptionsSelected.push(indivSkill)
              // console.log(indivSkill)
            }
          });
          // skillsOptionsSelected = element.skills
          return
        }
      });

      console.log('skill options selected',skillsOptionsSelected)

      let skillOptionsSelectedNames = []
      skillsOptionsSelected.forEach(element => {
        console.log(element)
        skillOptionsSelectedNames.push(element.name)
      }); 

      console.log(skillOptionsSelectedNames)

      this.skillOptions = skillOptionsSelectedNames


    },
    async onAssignSkillToJobRole(){
      if (this.skillOptions.length == 0){
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Must select at least 1 skill!'
        })
      }else{
        // have options, get the array of option IDs from skillOptions names
        console.log(this.skillOptions)

        let skillOptionIds = []
        this.skillData.forEach(element => {
          if (this.skillOptions.includes(element.name) ){
            skillOptionIds.push(element.id)
          }
        });


        console.log('job id',this.assignRowId,'skill option ids:',skillOptionIds)

        let assignRes = await axios.put(`http://127.0.0.1:5000/api/roles/${this.assignRowId}/skills`,{
          skill_ids:skillOptionIds
        })
        
        // console.log(assignRes)

        // this.skillOptions = []
        this.assignDialog = false
        this.getJobTable()
          
        this.$q.notify({
          icon: 'done',
          color: 'positive',
          icon:'done',
          message: 'Assigned skills to role'
        })



      }
    },
    async deleteJob(row){
      console.log(row)

      let deleteData = await axios.delete(`http://127.0.0.1:5000/api/roles/${row.id}`).catch(err=>{
        console.log(err)
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Failed to delete job'
        })
        return
      })

      this.$q.notify({
        icon: 'done',
        color: 'positive',
        icon:'done',
        message: 'Job Role Made Inactive'
      })

      // refresh table again
      this.getJobTable()


    },


    async getSkillTable(){
      let skillData = await axios.get('http://127.0.0.1:5000/api/skills')
      this.skillsEmpty = true

      let currSkillData = []

      skillData.data.forEach(element => {
        
          this.skillsEmpty = false
          currSkillData.push(element)
          
        
      });

      
      this.skillData = currSkillData
    },
    async onSkillSubmit () {
      this.$refs.skillName.validate()
      this.$refs.skillDescription.validate()

      if (this.$refs.skillName.hasError || this.$refs.skillDescription.hasError) {
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Inputs cannot be empty'
        })
      }
      else {

        // // add else if the name already inside database, throw error
        let nameExists = false
        this.skillData.forEach(element => {
          if (this.skillName == element.name){
            nameExists = true
            return
          }
        });

        if (nameExists == true){
          this.$q.notify({
            color: 'negative',
            icon:'error',
            message: `Skill: '${this.skillName}'' already inside database`
          })
        }else{
          let postSkillRes = await axios.post('http://127.0.0.1:5000/api/skills/',{
            name:this.skillName,
            description:this.skillDescription,
            active:true 
          }).catch(err=>{
            console.log(err)
            this.$q.notify({
              color: 'negative',
              icon:'error',
              message: 'Failed to add skill to database'
            })
            return
          })

          // refresh table again
          this.getSkillTable()

          
          this.addSkillDialog = false
          
          this.$q.notify({
            icon: 'done',
            color: 'positive',
            icon:'done',
            message: 'Skill Created'
          })
        }

        // reset every enter
        this.skillName=''
        this.skillDescription=''

       

       
      }

   
    },

    openEditSkillPopup(row){
      this.editSkillDialog = true
      this.editSkillName = row.name
      this.editSkillDescription = row.description
      this.editSkillId = row.id
      if (row.active == true){
        this.editSkillStatusOption = 'Active'
      }else{
        this.editSkillStatusOption = 'Inactive'
      }
      
      console.log(row)
    },
    async onEditSkill(){
      //basically same as onSubmit but instead of POST is PUT
      this.$refs.editSkillName.validate()
      this.$refs.editSkillDescription.validate()

      if (this.$refs.editSkillName.hasError || this.$refs.editSkillDescription.hasError) {
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Inputs cannot be empty'
        })
      }
      else {
        let jobStatus = ''
        if (this.editSkillStatusOption == 'Active'){
          jobStatus = true
        }else{
          jobStatus = false
        }

          let editSkillPass = true
          let updateRes = await axios.put(`http://127.0.0.1:5000/api/skills/${this.editSkillId}`,{
            name:this.editSkillName,
            description:this.editSkillDescription,
            active:jobStatus 
          }).catch(err=>{
            console.log('STATUS CODE',err.response.status)
            editSkillPass = false

            let errMessage = 'Failed to update skill in database'
            if (err.response.status == 400){
              errMessage = 'Skill name exists!'
            }
            this.$q.notify({
              color: 'negative',
              icon:'error',
              message: errMessage
            })
            return
          })

          // refresh table again
          this.getSkillTable()
          this.getJobTable()
          
          this.editSkillDialog = false
          
          if (editSkillPass == true){
            this.$q.notify({
              icon: 'done',
              color: 'positive',
              icon:'done',
              message: 'Edited Skill'
            })
          }
          
        }

        // reset every enter
        this.editSkilName=''
        this.editSkillDescription=''

    
    },

    async deleteSkill(row){
      let deleteData = await axios.delete(`http://127.0.0.1:5000/api/skills/${row.id}`).catch(err=>{
        console.log(err)
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Failed to delete skill'
        })
        return
      })

      this.$q.notify({
        icon: 'done',
        color: 'positive',
        icon:'done',
        message: 'Skill Made Inactive'
      })

      // refresh table again
      this.getJobTable()
      this.getSkillTable()

    }

    // need to make onEditSkillPopup and onEditSkill
  },
  data () {
    return {
      tab: 'View Job Roles',
      addJobDialog:false,
      jobRoleName:'',
      jobRoleDescription:'',
      accept: false,

      editJobDialog:false,
      editJobRoleName:'',
      editJobRoleDescription:'',
      editRowId:0,
      editJobStatusOption:'',

      assignDialog:false,
      assignJobRoleName:'',
      assignJobRoleDescription:'',
      assignRowId:0,
      skillOptionsArray:[], //for the skill options
      skillOptions:'skill1', //v-model


      addSkillDialog:false,
      skillName:'',
      skillDescription:'',

      editSkillDialog:false,
      editSkillName:'',
      editSkillDescription:'',
      editSkillId:0,
      editSkillStatusOption:'',

      //visibility of empty div. on mounted if have records then set this programatically to false.
      jobsEmpty:false,
      skillsEmpty:false,
      coursesEmpty:true,


      jobColumns: [
        {
          name: 'id',
          required: true,
          label: 'ID',
          align: 'left',
          field: 'id',
          sortable: true
        },
        { name: 'name', align: 'center', label: 'Job Role Name', field: 'name', sortable: true },
        { name: 'description', align: 'center', label: 'Job Role Description', field: 'description',style: "max-width:400px;white-space: normal;" },
        { name: 'skills', align: 'center', label: 'Job Role Skills', field: 'skills' },
        { name: 'status', align: 'center', label: 'Job Role Status', field: 'status' },
        { name: 'buttons', align: 'center', field: 'buttons' },
        
      ],

      jobData: [
        {
          id: 'JR001',
          name: 'Senior Engineer',
          description: 'A super pro developer',
          // skills: ['HTML','CSS','Javascript'],
          // buttons:''
          
        },
        {
          id: 'JR002',
          name: 'Junior Engineer',
          description: 'A noob developer',
          // skills: ['HTML'],
          // buttons:''
          
        },
        {
          id: 'JR003',
          name: 'Marketing Director',
          description: 'A marketing person',
          // skills: ['Excel', ' Powerpoint'],
          // buttons:''
          
        },
        
        
      ],

      skillColumns: [
        {
          name: 'id',
          required: true,
          label: 'ID',
          align: 'left',
          field: 'id',
          sortable: true
        },
        { name: 'name', align: 'center', label: 'Skill Title', field: 'name', sortable: true },
        { name: 'description', align: 'center', label: 'Skill Description', field: 'description', sortable: true },
        { name: 'status', align: 'center', label: 'Skill Status', field: 'status' },
        { name: 'buttons', align: 'center', field: 'buttons' },
        
      ],

      skillData: [
        {
          id: 'JR001',
          name: 'Senior Engineer',
          description: 'A super pro developer',
          // skills: ['HTML','CSS','Javascript'],
          // buttons:''
          
        },
        {
          id: 'JR002',
          name: 'Junior Engineer',
          description: 'A noob developer',
          // skills: ['HTML'],
          // buttons:''
          
        },
        {
          id: 'JR003',
          name: 'Marketing Director',
          description: 'A marketing person',
          // skills: ['Excel', ' Powerpoint'],
          // buttons:''
          
        },
        
        
      ],


      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true
      },
    }
  },
  name: 'Page1',
  components: {
    Lottie
  },
  async mounted(){
    // let roleData = await axios.get('http://127.0.0.1:5000/api/roles')
    // console.log(roleData.data)

    // this.jobsEmpty = true

    // roleData.data.forEach(element => {
    //   if (element.active == true){
    //     this.jobsEmpty = false
    //     return
    //   }
    // });

    
    // this.jobData = roleData.data

    this.getJobTable()
    this.getSkillTable()
      

  }
  
}
</script>

<style scoped>
.addButton{
  transition: 0.2s;
}

.addButton:hover{
  transform:translateY(-5px)
}
</style>