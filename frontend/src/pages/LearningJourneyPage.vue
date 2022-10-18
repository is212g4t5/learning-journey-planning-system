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
    console.log('vuex user',this.$store.state.user)
    console.log('storage token',localStorage.token)
    if (localStorage.token == undefined || localStorage.token != this.$store.state.user){
      this.$router.push('/login')
    }
    
  }
}
</script>
