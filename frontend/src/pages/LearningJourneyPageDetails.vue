<template>
  <q-page class="">

    <div class="q-px-md">
      <!-- {{currUserLearningJourney}} -->

      <q-breadcrumbs class="q-mt-md">
          <template v-slot:separator>
            <q-icon
              size="1.5em"
              name="chevron_right"
              color="primary"
            />
          </template>
          <q-breadcrumbs-el  >Learning Journeys</q-breadcrumbs-el>
          <q-breadcrumbs-el :to="`/learning_journey/${$store.state.user}`">View Learning Journeys</q-breadcrumbs-el>
          <q-breadcrumbs-el >{{currUserLearningJourney.name}}</q-breadcrumbs-el>
         
        </q-breadcrumbs>

        <div
          class="text-center font-700 q-mt-md"
          style="color: #525252; font-size: 28px; "
        >
          View Courses in {{currUserLearningJourney.name}}
        </div>
        <div
          class="q-mx-auto q-mb-lg"
          style="background-color: #a8a8ff; width: 75px; height: 2px"
        ></div>


        <q-btn label="Add Course To Learning Journey" color="primary" no-caps class="addButton absolute" style="right:30px; top:30px;z-index:1" :to="`/filtered_courses/${currUserLearningJourney.id}`" ></q-btn>

      <div class="flex items-center justify-around q-mb-md">
        <div v-for="course in currUserLearningJourney.courses" :key="course.id" style="width:350px;height:580px;background:white;border-radius:5px;position:relative;" class="shadow-4">
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
                    <div class="q-mb-sm">
                      <q-icon name="place" size="sm" style="color:#96BB7C"></q-icon>
                      {{course.type}}
                    </div>
                   

                    <div v-if="course.status=='Active'" class="q-pa-sm text-center" style="background:#96BB7C; border-radius:10px">{{course.status}}</div>
                    <div v-else-if="course.status=='Pending'" class="q-pa-sm text-center text-white" style="background:#E59749; border-radius:10px">{{course.status}}</div>
                    <div v-else class="q-pa-sm text-center text-white" style="background:red; border-radius:10px">{{course.status}}</div>
                  </div>
                 
                  <q-btn v-if="currUserLearningJourney.courses.length>1" label="delete" color="red" @click="openDeleteDialog(course)"></q-btn>
                </div>

               
           </div>
          

           
          </div>
          
        </div>
      </div>
   

    </div>


    <q-dialog v-model="deleteDialog">
      <q-card class="q-pa-md" style="width:50vw">
        <div class="text-center font-700" style="color:#525252; font-size:28px">Delete Course From Learning Journey</div>
        <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

        

        
        <div class="q-mx-md">
          Are you sure you want to delete <strong>{{currentCourse.name}}</strong> from <strong>{{currUserLearningJourney.name}}</strong>?
          
        </div>
        

        <q-card-actions align="right" class="q-mt-sm">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn  label="Delete Learning Journey" color="primary" @click="deleteCourseFromLJ()"/>
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
      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true
      },


      currUserLearningJourney:[],
      deleteDialog:false,
      currentCourse:{}
    }
  },
  components: {
    Lottie
  },
  methods: {
    openDeleteDialog(course){
      this.currentCourse = course
      this.deleteDialog = true
    },

   async deleteCourseFromLJ(){
    let deleteRes = await axios.delete(`http://127.0.0.1:5000/api/learning_journeys/${this.$route.params.id}/courses/${this.currentCourse.id}`)
    console.log(deleteRes.data)

    let learningJourney_data = await axios.get(`http://127.0.0.1:5000/api/learning_journeys/${this.$route.params.id}`)
    console.log(learningJourney_data.data)
    this.currUserLearningJourney = learningJourney_data.data

    this.deleteDialog = false
   }
  },
  async mounted(){
    console.log('vuex user',this.$store.state.user)
    console.log('storage token',localStorage.token)
    if (localStorage.token == undefined){
      this.$router.push('/login')
    }


    let learningJourney_data = await axios.get(`http://127.0.0.1:5000/api/learning_journeys/${this.$route.params.id}`)
    console.log(learningJourney_data.data)

    this.currUserLearningJourney = learningJourney_data.data

    
  }
}
</script>
<style>
.ljCard{
  transition:0.3s;
  border-radius:10px;
  cursor:pointer;
}

.ljCard:hover{
  transform:translateY(-5px);
  box-shadow: rgb(254 153 2) 0px 0px 20px;
}
</style>