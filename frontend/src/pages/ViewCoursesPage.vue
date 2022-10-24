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

                <div class="q-mt-md">
                <q-icon name="place" size="sm" style="color:#96BB7C"></q-icon>
                {{course.type}}
                </div>
           </div>
          

           
          </div>
          
        </div>
      </div>
     



    </div>
    
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
      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true
      },
    }
  },
  components: {
    Lottie
  },
  methods: {
  },
  async mounted(){
    // console.log('vuex user',this.$store.state.user)
    // console.log('storage token',localStorage.token)
    // if (localStorage.token == undefined){
    //   this.$router.push('/login')
    // }

      console.log('USR DATA FROM COURSES PAGE:',this.$store.state.userData)



    let courseData = await axios.get("http://127.0.0.1:5000/api/courses/active/skills");
    console.log('active course data', courseData.data)

    
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

    console.log('all courses with skill:',coursesWithSkill)
    console.log('current skill details:',currSkillInfo)

    this.coursesWithSkill = coursesWithSkill


    let allSkills = await axios.get("http://127.0.0.1:5000/api/skills");

    console.log('all skill data:', allSkills)
    allSkills.data.forEach(element => {
      if (element.id == currSkillId){
        this.currSkillInfo = element
      }
    });

    // this.currSkillInfo = currSkillInfo
    console.log()
   
    
  }
}
</script>
