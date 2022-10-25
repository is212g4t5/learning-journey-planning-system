<template>
  <q-page class="">
    <div class="text-center" v-if="currUserLearningJourney.length == 0" >
      <div class="text-center font-700" style="color:#525252; font-size:28px">Hello {{$store.state.userData.first_name}}  {{$store.state.userData.last_name}} </div>
      <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>
      <Lottie :options="defaultOptions" style="width:20vw" />
      <div class="font-700 font-size-28">No Learning Journey Created!</div>
      <div class="font-500 font-size-14 myTextGrey">You have yet to create any learning journey.</div>
    </div>



    <div v-else class="">
      {{currUserLearningJourney}}


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

    let currUserLearningJourney = []

    let learningJourney_data = await axios.get('http://127.0.0.1:5000/api/learning_journeys/')
    console.log('all learning journey data', learningJourney_data.data)

    learningJourney_data.data.forEach(element => {
      if (element.staff_id == this.$store.state.userData.id){
        currUserLearningJourney.push(element)
      }
    });

    this.currUserLearningJourney = currUserLearningJourney
    
    console.log('USE DATA FROM COURSES PAGE:',this.$store.state.userData)
    
  }
}
</script>
