<template>
  <q-page class="">
    <q-breadcrumbs class="q-mt-md q-px-xl">
      <template v-slot:separator>
        <q-icon
          size="1.5em"
          name="chevron_right"
          color="primary"
        />
      </template>
      <q-breadcrumbs-el to="/Jobs" >Job Roles</q-breadcrumbs-el>
      <q-breadcrumbs-el to="/Jobs">View Job Roles</q-breadcrumbs-el>
      <q-breadcrumbs-el to="">{{currSkillInfo.name}}</q-breadcrumbs-el>
      <q-breadcrumbs-el to="">View Courses</q-breadcrumbs-el>
    </q-breadcrumbs>

    <div class="q-mt-md q-px-md" style="background:#EFF8ED;padding-bottom:140px">
      <div class="text-center" style="color:#007AFF;font-size:50px;font-weight:600">{{currSkillInfo.name}}</div>

      <div
        class="text-center font-700"
        style="color: #525252; font-size: 28px; "
      >
        Recommended Courses
      </div>
      <div
        class="q-mx-auto q-mb-lg"
        style="background-color: #a8a8ff; width: 75px; height: 2px"
      ></div>

      <q-btn label="Create Learning Journey" color="primary" class="absolute" style="right:40px; top:75px" @click="createLJ = !createLJ"></q-btn>


      <div class="text-center" v-if="coursesWithSkill.length==0">
        <Lottie :options="defaultOptions" style="width:20vw" />
        <div class="font-700 font-size-28">No Courses Offered For {{currSkillInfo.name}} Yet !</div>
        <div class="font-500 font-size-14 myTextGrey">Please check back another time.</div>
      </div>
      


      <div class="flex items-center justify-around">
        <div v-for="course in coursesWithSkill" :key="course.id" class="" style="width:350px;height:550px;background:white;border-radius:5px;position:relative">
          <img src="~assets/courseImage.png" style="width:100%;border-top-left-radius:5px;border-top-right-radius:5px" alt="">
          <div class="q-px-md q-py-sm">
            <div class="q-mb-sm" style="font-size:20px;font-weight:700">{{course.name}}</div>
            <div class="q-mb-sm" style="color:#676767;font-size:16px;font-weight:700">{{course.category}} ({{course.id}})</div>
            <div class="" style="color:#737373; font-size:14px">{{course.description}}</div>

           <div class="" style="position:absolute;bottom:20px">
              <!-- buttons div -->
              <div class="flex items-center q-gutter-x-sm q-mt-md">

                <div v-for="skill in course.skills" :key="skill.id" class="" style="">
                  <div v-if="skill.id == currSkillId" class="q-pa-sm" style="background:#96BB7C; border-radius:10px">{{skill.name}}</div>
                  <div v-else class="q-pa-sm" style="background:#E6E6E6; border-radius:10px">{{skill.name}}</div>

                </div>
                </div>

                <div class="q-mt-md flex justify-between items-center" style="width:300px">
                  <div class="">
                    <q-icon name="place" size="sm" style="color:#96BB7C"></q-icon>
                    {{course.type}}
                  </div>
                 
                  <q-checkbox v-model="selection" :val="course.id" label="Select course" color="green" />
                </div>

               
           </div>
          

           
          </div>
          
        </div>
      </div>
     



    </div>

     <!-- add skill dialog -->
     <q-dialog v-model="createLJ">
          <q-card class="q-pa-md" style="width:50vw">
            <div class="text-center font-700" style="color:#525252; font-size:28px">Create Learning Journey</div>
            <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

           

            
            <div class="q-mx-md">
              Do you want to create learning joruney for <strong>Senior Engineer</strong>?
              <br>
              Courses that will be added to learning journey: <span v-for="course in selection" :key="course"> <strong>{{course}} </strong> </span>
            </div>
            

            <q-card-actions align="right" class="q-mt-sm">
              <q-btn flat label="Cancel" color="primary" v-close-popup />
              <q-btn  label="Create Learning Journey" color="primary" @click="handleCreate()"/>
            </q-card-actions>

            
          </q-card>
        </q-dialog>
    
  </q-page>
</template>

<script>
import axios from "axios";
import Lottie from 'vue-lottie';
import * as animationData from './empty.json';
export default {
  data () {
    return {
      currSkillInfo:{},
      coursesWithSkill:[],
      currSkillId:'',
      currJobId:'',
      jobData:{},
      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true,
      },

      selection:[],
      createLJ:false
    }
  },
  components: {
    Lottie
  },
  methods: {
    async handleCreate(){
      console.log('input to post',{
        name:"Learning Journey - " + this.jobData.name,
        staff_id:this.$store.state.userData.id,
        role_id:Number(this.currJobId),
        course_ids:this.selection
      })

  

      let createLJ_res = await axios.post("http://127.0.0.1:5000/api/learning_journeys/create",{
        name:"Learning Journey - " + this.jobData.name,
        staff_id:this.$store.state.userData.id,
        role_id:Number(this.currJobId),
        course_ids:this.selection
      });

      console.log(createLJ_res)
    }
  },
  async mounted(){
    // console.log('vuex user',this.$store.state.user)
    // console.log('storage token',localStorage.token)
    // if (localStorage.token == undefined){
    //   this.$router.push('/login')
    // }

    console.log('USE DATA FROM COURSES PAGE:',this.$store.state.userData)



    let courseData = await axios.get("http://127.0.0.1:5000/api/courses/active/skills");
    // console.log('active course data', courseData.data)

    this.currJobId =  this.$route.params.jobId

    let currSkillId = this.$route.params.skillId
    this.currSkillId = currSkillId

    let currSkillInfo = {}
    let coursesWithSkill = []

    courseData.data.forEach(element => {
        if (element.skills.length>0){
          element.skills.forEach(skill => {
            if (skill.id == currSkillId && skill.active == true){
              coursesWithSkill.push(element)
             
            }
          });
        }
    });

    this.coursesWithSkill = coursesWithSkill

    let allSkills = await axios.get("http://127.0.0.1:5000/api/skills");
    allSkills.data.forEach(element => {
      if (element.id == currSkillId){
        this.currSkillInfo = element
      }
    });


    let roleData = await axios.get("http://127.0.0.1:5000/api/roles");
    console.log('JOB ROLE DATA', roleData.data)
    roleData.data.forEach((element) => {
      if (element.id == this.currJobId) {
        this.jobData = element
      }
    });


   
    
  }
}
</script>
