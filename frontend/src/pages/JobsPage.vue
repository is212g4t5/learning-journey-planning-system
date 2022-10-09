<template>
  <q-page class="q-px-xl">
    <div
      class="text-center font-700"
      style="color: #525252; font-size: 28px; margin-top: 30px"
    >
      View Job Roles
    </div>
    <div
      class="q-mx-auto q-mb-lg"
      style="background-color: #a8a8ff; width: 75px; height: 2px"
    ></div>

    <div v-for="job in jobData" :key="job.id" class="q-pa-md q-mt-md" style="background: #f5f5f5;cursor:pointer">
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
export default {
  data() {
    return {
      jobData: [],
    };
  },
  async mounted() {
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
