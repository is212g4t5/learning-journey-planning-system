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
      <q-breadcrumbs-el to="/Jobs">View Job Roles</q-breadcrumbs-el>
      <q-breadcrumbs-el to="">{{jobData.name}}</q-breadcrumbs-el>
    </q-breadcrumbs>

    <div
      class="text-center font-700"
      style="color: #525252; font-size: 28px; "
    >
      View Job Role Details
    </div>
    <div
      class="q-mx-auto q-mb-lg"
      style="background-color: #a8a8ff; width: 75px; height: 2px"
    ></div>

    <div class="q-pa-md q-mt-md" style="background: #f5f5f5">
      <div class="flex  no-wrap" >
        <div class="q-mr-md flex justify-center items-center" style="background: #d9d9d9;">
          <q-icon name="o_person" style="font-size:200px; padding:30px"></q-icon>

        </div>

        <div class="q-pa-md">
          <div class="" style="font-size:40px;font-weight:500">{{jobData.name}}</div>
          <div class="text-grey-7" style="font-size:24px">Job Description:</div>
          <div class="q-mb-lg" style="font-size:18px">
            {{jobData.description}}
          </div>

          <div class="text-grey-7" style="font-size:24px">Skills Required:</div>
          <div v-if="noSkills" class="font-size:24px">Hey there! There are no skills required for <strong>{{jobData.name}}</strong></div>
          

          <div class="row">
            <div v-for="skill in jobData.skills" :key="skill.name" class="q-pa-sm" >
              <q-btn v-if="skill.active==true" @click="redirectToCoursePage(skill)">{{skill.name}}</q-btn>
            </div>
            

          </div>
        </div>
      </div>
    </div>

   
  </q-page>
</template>

<script>
import axios from "axios";
export default {
  methods: {
    redirectToCoursePage(skill){
      console.log(skill)
      this.$router.push(`/courses/${skill.id}`)
    }
  },
  data() {
    return {
      jobData: {},
      noSkills:true
    };
  },
  async mounted() {
    let roleData = await axios.get("http://127.0.0.1:5000/api/roles/skills");
    
    let currJobData = null;
    roleData.data.forEach((element) => {
      if (element.id == this.$route.params.id) {
        currJobData=element
        return
      }
    });

    this.jobData = currJobData;
    
    this.jobData.forEach(element => {
      element.skills.forEach(skill => {
        if (skill.active == true){
          this.noSkills = false
          return
        }
      });
    });

    console.log("job data:", this.jobData);
  },
};
</script>
