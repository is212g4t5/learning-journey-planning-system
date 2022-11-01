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
      <q-breadcrumbs-el to="" >{{currUserLearningJourney.name}}</q-breadcrumbs-el>
      <q-breadcrumbs-el :to="`/learning_journey/${$store.state.user}/${this.$route.params.LJ_id}`">Add Course To Learning Journey</q-breadcrumbs-el>
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
        <div class="font-700 font-size-28">No Courses Offered For {{currUserLearningJourney.name}} Yet !</div>
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
                 
                  <q-btn label="Add Course" color="green" outline @click="addCourse(course)"></q-btn>
                </div>

               
           </div>
          

           
          </div>
          
        </div>
      </div>
     



    </div>



    <q-dialog v-model="addDialog">
      <q-card class="q-pa-md" style="width:50vw">
        <div class="text-center font-700" style="color:#525252; font-size:28px">Add Course To Learning Journey</div>
        <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

        

        
        <div class="q-mx-md">
          Are you sure you want to add <strong>{{currentCourse.name}}</strong> to <strong>{{currUserLearningJourney.name}}</strong>?
          
        </div>
        

        <q-card-actions align="right" class="q-mt-sm">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn  label="Add Course to Learning Journey" color="primary" @click="addCourseToDB()"/>
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

      addDialog:false,
      currentCourse:{},
      currUserLearningJourney:[],



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
      fail:false,

    
      createLJ:false
    }
  },
  components: {
    Lottie
  },
  methods: {
    async addCourse(course){
      console.log(course)
      this.currentCourse = course

      this.addDialog = true;
    },

    async addCourseToDB(){
      await axios.put(`http://127.0.0.1:5000/api/learning_journeys/${this.$route.params.LJ_id}`,
        {
          course_ids:[this.currentCourse.id]
        }
      )

      //reset data
      let courseData = await axios.get(`http://127.0.0.1:5000/api/learning_journeys/${this.$route.params.LJ_id}?courses_not_in_lj=true`)
      console.log('relevant courses not in lj',courseData.data)
      this.coursesWithSkill = courseData.data

      
      this.addDialog = false
    }

    
    
  },
  async mounted(){
    let courseData = await axios.get(`http://127.0.0.1:5000/api/learning_journeys/${this.$route.params.LJ_id}?courses_not_in_lj=true`)
    console.log('relevant courses not in lj',courseData.data)

    this.coursesWithSkill = courseData.data

    console.log('USE DATA FROM COURSES PAGE:',this.$store.state.userData)



    let learningJourney_data = await axios.get(`http://127.0.0.1:5000/api/learning_journeys/${this.$route.params.LJ_id}`)
    console.log('my current learning journey data',learningJourney_data.data)

    this.currUserLearningJourney = learningJourney_data.data
    console.log('curr user joruney', this.currUserLearningJourney)


   

   
    
  }
}
</script>
