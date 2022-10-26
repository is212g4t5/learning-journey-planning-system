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
<!--       

      <div v-for="LJ in currUserLearningJourney" :key="LJ.id" class="flex shadow-3 q-mt-md ljCard" style="">
        <img src="~assets/courseImage.png" alt="" style="width:300px;border-top-left-radius:10px;border-bottom-left-radius:10px;">

        <div class="q-pl-lg q-py-sm">
          <div class="" style="color:#767676;font-weight:500; font-size:24px">{{LJ.name}}</div>
          <div class="" style="color:#333333; font-weight:600; font-size:32px">{{LJ.name.split('-')[1]}}</div>


          <q-btn label="view" color="green" outline icon-right="keyboard_arrow_right" class="q-mr-sm q-mt-md" ></q-btn>
          <q-btn label="delete" color="red" outline class="q-mt-md" @click="openDeleteDialog(LJ)"></q-btn>
        </div>
      </div> -->


      <div class="flex items-center justify-around q-mb-md">
        <div v-for="course in currUserLearningJourney.courses" :key="course.id" style="width:350px;height:550px;background:white;border-radius:5px;position:relative;" class="shadow-4">
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
                 
                  <q-btn label="delete" color="red"></q-btn>
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
      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true
      },


      currUserLearningJourney:[]
    }
  },
  components: {
    Lottie
  },
  methods: {
   
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