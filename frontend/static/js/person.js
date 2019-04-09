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
        const signups = await data.signups
        this.signups = await signups
        },
        async getCreated(){
            const resp = await axios.get(`/events/createdby/${username}`);
            const data = await resp.data;
            const created = await data.created;
            this.created = await created;
        }

    },
    delimiters:['${','}'],
    created(){
       this.getSignups()
       this.getCreated()
    }
  })