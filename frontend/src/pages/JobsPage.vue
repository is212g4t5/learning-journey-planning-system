<template>
  <q-page class="q-px-xl">
    <q-breadcrumbs class="q-mt-md">
      <template v-slot:separator>
        <q-icon
          size="1.5em"
          name="chevron_right"
          color="primary"
        />
      </template>
      <q-breadcrumbs-el to="/Jobs" >Job Roles</q-breadcrumbs-el>
      <q-breadcrumbs-el>View Job Roles</q-breadcrumbs-el>
    </q-breadcrumbs>
    <div
      class="text-center font-700"
      style="color: #525252; font-size: 28px; "
    >
      View Job Roles
    </div>
    <div
      class="q-mx-auto q-mb-lg"
      style="background-color: #a8a8ff; width: 75px; height: 2px"
    ></div>

    <div class="text-center" v-if="jobData.length==0">
        <Lottie :options="defaultOptions" style="width:20vw" />
        <div class="font-700 font-size-28">No Roles Found!</div>
        <div class="font-500 font-size-14 myTextGrey">There are no roles in the system.</div>
      </div>


    <div v-for="job in jobData" :key="job.id" class="q-pa-md q-mt-md" style="background: #f5f5f5;cursor:pointer" @click="$router.push(`/JobDetails/${job.id}`)">
      <div class="flex  no-wrap" >
        <div class="q-pa-lg q-mr-md" style="background: #d9d9d9">
          <q-icon name="o_person" style="font-size:125px"></q-icon>

        </div>

        <div class="">
          <div class="" style="font-size:24px;font-weight:600">{{job.name}}</div>
          <div class="text-grey-7">Job Description:</div>
          <div class="q-mb-lg">
            {{job.description}}
          </div>

          <q-btn  rounded >
            <div class="flex items-center">
              <div class="q-mr-xs">
              View Job Role
              </div>
              
              <q-icon name="keyboard_arrow_right"></q-icon>
            </div>
            
          </q-btn>
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
  data() {
    return {
      jobData: [],
      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true
      },
    };
  },
  components: {
    Lottie
  },
  async mounted() {
    console.log('job page user',localStorage.token == undefined)
    if (localStorage.token == undefined || localStorage.token == ''){
      this.$router.push('/login')
    }


    let roleData = await axios.get("http://127.0.0.1:5000/api/roles");
    this.jobsEmpty = true;
    let currJobData = [];
    roleData.data.forEach((element) => {
      if (element.active == true) {
        this.jobsEmpty = false;
        currJobData.push(element);
      }
    });

    this.jobData = currJobData;
    console.log("job data:", this.jobData);
  },
};
</script>
