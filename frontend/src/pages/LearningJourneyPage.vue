<template>
  <q-page class="">
    <div class="text-center" v-if="currUserLearningJourney.length == 0" >
      <div class="text-center font-700" style="color:#525252; font-size:28px">Hello {{$store.state.userData.first_name}}  {{$store.state.userData.last_name}} </div>
      <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>
      <Lottie :options="defaultOptions" style="width:20vw" />
      <div class="font-700 font-size-28">No Learning Journey Created!</div>
      <div class="font-500 font-size-14 myTextGrey">You have yet to create any learning journey.</div>
    </div>



    <div v-else class="q-px-md">
      <!-- {{currUserLearningJourney}} -->

      <div v-for="LJ in currUserLearningJourney" :key="LJ.id" class="flex shadow-3 q-mt-md ljCard" style="">
        <img src="~assets/learning_journey.jpg" alt="" style="width:300px;border-top-left-radius:10px;border-bottom-left-radius:10px;">

        <div class="q-pl-lg q-py-sm">
          <div class="" style="color:#767676;font-weight:500; font-size:24px">{{LJ.name}}</div>
          <div class="" style="color:#333333; font-weight:600; font-size:32px">{{LJ.name.split('-')[1]}}</div>


          <q-btn label="view" color="green" outline icon-right="keyboard_arrow_right" class="q-mr-sm q-mt-md"></q-btn>
          <q-btn label="delete" color="red" outline class="q-mt-md" @click="openDeleteDialog(LJ)"></q-btn>
        </div>
      </div>
   

    </div>




    <q-dialog v-model="deleteDialog">
      <q-card class="q-pa-md" style="width:50vw">
        <div class="text-center font-700" style="color:#525252; font-size:28px">Delete Learning Journey</div>
        <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:85px;height:2.5px"></div>

        

        
        <div class="q-mx-md">
          Are you sure you want to delete <strong>{{LJ.name}}</strong>?
          
        </div>
        

        <q-card-actions align="right" class="q-mt-sm">
          <q-btn flat label="Cancel" color="primary" v-close-popup />
          <q-btn  label="Delete Learning Journey" color="primary" @click="handleDelete()"/>
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
      deleteDialog:false,
      LJ:{},


      currUserLearningJourney:[]
    }
  },
  components: {
    Lottie
  },
  methods: {
    openDeleteDialog(LJ){
      this.LJ = LJ
      this.deleteDialog = !this.deleteDialog
    },
    async handleDelete(){
      // let deleteRes = await axios.delete('')
    }
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