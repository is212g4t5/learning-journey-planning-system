<template>
  <q-page class="">

    <q-breadcrumbs class="q-ml-md q-mt-md">
      <template v-slot:separator>
        <q-icon
          size="1.5em"
          name="chevron_right"
          color="primary"
        />
      </template>
      <q-breadcrumbs-el to="/HR" >HR Management</q-breadcrumbs-el>
      <q-breadcrumbs-el>{{tab}}</q-breadcrumbs-el>
    </q-breadcrumbs>

    <div class="text-center font-700" style="color:#525252; font-size:28px">HR Management</div>
    <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:75px;height:2px"></div>

    <q-tabs
        v-model="tab"
        align="justify"
        narrow-indicator
        class="text-grey-9" 
        active-class="text-primary"
        style="border-bottom:1px solid grey"
      >
        <q-tab class="" name="View Job Roles" label="View Job Roles" no-caps />
        <q-tab class="" name="View Skills" label="View Skills" no-caps />
        <q-tab class="" name="View Courses" label="View Courses" no-caps/>
      </q-tabs>

      <q-tab-panels
          v-model="tab"
          animated
          transition-prev="fade"
          transition-next="fade"
          class=""
        >
        <!-- job roles panel -->
          <q-tab-panel name="View Job Roles">
            <q-btn label="Add New Role" color="primary" no-caps class="addButton absolute" style="right:20px"></q-btn>
            <div class="text-center" v-show="jobsEmpty">
              <Lottie :options="defaultOptions"  v-on:animCreated="handleAnimation" style="width:20vw" />
              <div class="font-700 font-size-28">No Roles Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>
          </q-tab-panel>

          <!-- skills panel -->
          <q-tab-panel name="View Skills" v-show="skillsEmpty">
            <q-btn label="Add New Skill" color="primary" no-caps class="addButton absolute" style="right:20px"></q-btn>
            <div class="text-center">
              <Lottie :options="defaultOptions"  v-on:animCreated="handleAnimation" style="width:20vw" />
              <div class="font-700 font-size-28">No Skills Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>
          </q-tab-panel>


          <!-- courses panel -->
          <q-tab-panel name="View Courses" v-show="coursesEmpty">
            
            <div class="text-center">
              <Lottie :options="defaultOptions"  v-on:animCreated="handleAnimation" style="width:20vw" />
              <div class="font-700 font-size-28">No Courses Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>
          </q-tab-panel>
        </q-tab-panels>
    
    
    
  </q-page>
</template>

<script>
import Lottie from 'vue-lottie';
import * as animationData from './empty.json';
export default {
  data () {
    return {
      tab: 'View Job Roles',

      //visibility of empty div. on mounted if have records then set this programatically to false.
      jobsEmpty:true,
      skillsEmpty:true,
      coursesEmpty:true,



      defaultOptions: {
        animationData: animationData.default,
        loop:true,
        autoplay:true
      },
    }
  },
  name: 'Page1',
  components: {
    Lottie
  },
  
}
</script>

<style scoped>
.addButton{
  transition: 0.2s;
}

.addButton:hover{
  transform:translateY(-5px)
}
</style>