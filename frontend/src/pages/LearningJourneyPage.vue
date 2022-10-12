<template>
  <q-page class="flex flex-center">
    <h1>Learning Journey Page</h1>
  </q-page>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  methods: {
  },
  mounted(){
    
    console.log('params route:',this.$router.currentRoute.params.role)
  }
}
</script>
