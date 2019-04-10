var app = new Vue({
    components:{
    },
    el: '#app',
    data: {
      signups:null,
      created:null,
    },
    methods:{
       async getSignups(){
        const resp = await axios.get(`/events/usersignups/${username}`);
        const data = await resp.data;
        this.signups = await data
        console.log(data)
        },
        async getCreated(){
            const resp = await axios.get(`/events/createdby/${username}`);
            const data = await resp.data;
            this.created = await data;
        }

    },
    delimiters:['${','}'],
    created(){
       this.getSignups()
       this.getCreated()
    }
  })