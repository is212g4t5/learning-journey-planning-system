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
                  <q-badge v-for="(skill,index) in props.row.skills" :key="index" color="orange" class="q-mr-xs">
                    {{skill}}
                  </q-badge>
                </q-td>

                <q-td key="buttons" :props="props" class="q-gutter-x-sm">
                    <q-btn label="Edit" color="orange" outline no-caps @click="editJob(props.row)"></q-btn>
                    <q-btn label="Assign" color="green" outline no-caps @click="assignJob(props.row)"></q-btn>
                    <q-btn label="Delete" color="red" outline no-caps @click="deleteJob(props.row)"></q-btn>
                </q-td>
                
              </q-tr>
            </template>
          </q-table>
          </q-tab-panel>

          <!-- skills panel -->
          <q-tab-panel name="View Skills" >
            <q-btn label="Add New Skill" color="primary" no-caps class="addButton absolute" style="right:30px; top:30px;z-index:1"></q-btn>
            <div class="text-center" v-if="skillsEmpty">
              <Lottie :options="defaultOptions"  style="width:20vw" />
              <div class="font-700 font-size-28">No Skills Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>
          </q-tab-panel>


          <!-- courses panel -->
          <q-tab-panel name="View Courses" v-show="coursesEmpty">
            
            <div class="text-center" v-if="skillsEmpty">
              <Lottie :options="defaultOptions"  style="width:20vw" />
              <div class="font-700 font-size-28">No Courses Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>
          </q-tab-panel>
        </q-tab-panels>
    
        

        <q-dialog v-model="addJobDialog">
          <q-card class="q-pa-md" style="width:50vw">
            <div class="text-center font-700" style="color:#525252; font-size:28px">Add Job Role</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

            <form @submit.prevent.stop="addJob" >
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
              <q-btn  label="Create" color="primary" type="submit" />
            </q-card-actions>

            </form>
          </q-card>
        </q-dialog>

    
  </q-page>
</template>

<script>
import Lottie from 'vue-lottie';
import * as animationData from './empty.json';
export default {
  methods: {
    async addJob() {
      this.$refs.jobRoleName.validate()
      this.$refs.jobRoleDescription.validate()

      if (this.$refs.jobRoleName.hasError || this.$refs.jobRoleDescription.hasError) {
        this.$q.notify({
          color: 'negative',
          icon:'error',
          message: 'Inputs cannot be empty'
        })

        return
      }
      // // add else if the name already inside database, throw error
      // else if(){

        // return
      // }
      else {
        this.addJobDialog = false

        // await axios.post

        this.$q.notify({
          icon: 'done',
          color: 'positive',
          icon:'done',
          message: 'Submitted'
        })

        this.jobRoleName=''
        this.jobRoleDescription=''
      }

      
    },

    editJob(row){
      console.log(row)
    },
    
    assignJob(row){
      console.log(row)
    },
    deleteJob(row){
      console.log(row)
    }
  },
  data () {
    return {
      tab: 'View Job Roles',
      addJobDialog:false,
      jobRoleName:'',
      jobRoleDescription:'',
      accept: false,

      //visibility of empty div. on mounted if have records then set this programatically to false.
      jobsEmpty:false,
      skillsEmpty:true,
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
        { name: 'description', align: 'center', label: 'Job Role Description', field: 'description', sortable: true },
        { name: 'skills', align: 'center', label: 'Job Role Skills', field: 'skills' },
        { name: 'buttons', align: 'center', field: 'buttons' },
        
      ],

      jobData: [
        {
          id: 'JR001',
          name: 'Senior Engineer',
          description: 'A super pro developer',
          skills: ['HTML','CSS','Javascript'],
          buttons:''
          
        },
        {
          id: 'JR002',
          name: 'Junior Engineer',
          description: 'A noob developer',
          skills: ['HTML'],
          buttons:''
          
        },
        {
          id: 'JR003',
          name: 'Marketing Director',
          description: 'A marketing person',
          skills: ['Excel', ' Powerpoint'],
          buttons:''
          
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