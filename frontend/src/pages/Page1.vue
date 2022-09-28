<template>
  <q-page class="">

    <div class="text-center font-700" style="color:#525252; font-size:30px">HR Management</div>
    <div class="q-mx-auto q-mb-md" style="background-color:#A8A8FF; width:75px;height:2px"></div>

    <q-tabs
        v-model="tab"
        align="justify"
        narrow-indicator
        class="text-grey-9" 
        active-class="text-primary"
        style="border-bottom:1px solid grey"
      >
        <q-tab class="" name="roles" label="View Job Roles" />
        <q-tab class="" name="skills" label="View Skills" />
        <q-tab class="" name="courses" label="View Courses" />
      </q-tabs>

      <q-tab-panels
          v-model="tab"
          animated
          transition-prev="fade"
          transition-next="fade"
          class="text-center"
        >
          <q-tab-panel name="roles">
            <div class="text-center">
              <Lottie :options="defaultOptions"  v-on:animCreated="handleAnimation" style="width:20vw" />
              <div class="font-700 font-size-28">No Roles Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>
          </q-tab-panel>

          <q-tab-panel name="skills">
            <div class="text-center">
              <Lottie :options="defaultOptions"  v-on:animCreated="handleAnimation" style="width:20vw" />
              <div class="font-700 font-size-28">No Skills Found!</div>
              <div class="font-500 font-size-14 myTextGrey">There are no roles in the system. Start adding <br> new roles to view them.</div>
            </div>
          </q-tab-panel>

          <q-tab-panel name="courses">
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
      tab: 'roles',
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
