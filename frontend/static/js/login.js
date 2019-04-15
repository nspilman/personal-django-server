var app = new Vue({
    components:{
    },
    el: '#login-form',
    data: {
      events:null,
      username:null,
      password:null,
      loggedIn:false,
    },
    methods:{
        async loginStatus(){
            const resp = await axios.get('/events/login/')
            const data = await resp.data
            this.loggedIn = await data
        },
        async postLogin(){
          const resp = await axios.post(
                '/events/login/',
                {
                    username:this.username,
                    password:this.password
                }
            )
            const status = await resp.status
            if (status === 200){
                this.loggedIn = true;
            }
            console.log(status)
        },
        async postLogout(){
            const resp = await axios.get('/events/logout/')
              const status = await resp.status
              if (status === 200){
                  this.loggedIn = false;
              }
              console.log(status)
          }
        
    },
    delimiters:['${','}'],
    created(){
        this.loginStatus()
    },
  })

  