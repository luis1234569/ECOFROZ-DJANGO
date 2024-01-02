var app = Vue.createApp(
  {
data() {
     return {
    mensaje: "Debe seleccionar un sector válido!",
    contador:0,
    var:'',
    kword:'',
    opcion_elegida:'',
    lista_sectores: [],
    elementos_invalidos: [{area_codigo: 0, area_nombre: 'DEBE SELECCIONAR UN SECTOR VALIDO!', area_estado: 1, area_ubica: 0, area_departamento: 0}]
  }
},

compilerOptions: {
  delimiters: ["${", "}$"]
 },

watch: {
  kword: function(val){
    this.BuscarSectores(val);
  }

},
methods:{
  BuscarSectores: function (kword){
    var self = this;
    axios.get('/trabajosinternos/api/consultasector/?kword=' + kword )
      .then(function(response){
        
        if (self.contador == 0){
        self.lista_sectores = response.data;
        console.log(response.data);
        if(response.data == 0){
          self.lista_sectores = self.elementos_invalidos
          self.kword = ""
        }
        
        
        }
        else
        if(kword != self.var ){
          self.lista_sectores = response.data;
          
        } 
        else
        self.lista_sectores = [];
        

      })
      .catch(function(error){
        console.log(error);

      })
  },
  AgregarSector: function(sector){
    var self = this;
    self.contador = self.contador + 1;
    // self.lista_sectores = [];   
    self.lista_sectores = [];
    self.kword = sector
    self.var = sector
  
    
    
    
  }

}, 

}
).mount('#vueapp');








// var app = Vue.createApp({
//     data() {return {
//     mensaje:'',
//     newmasdetalles: '',
//     lista_agregados: [],
//     lista_opciones: []
//     }},
//     compilerOptions: {
//       delimiters: ["${", "}$"]
//     },
//     watch:{
//       newmasdetalles: function(val){
//         this.ListarOpciones(val);
//       }

//     },

//     methods: {
//       ListarOpciones: function (kword) {
//         var self = this;
//         axios.get('/recepcionmp/api/mas_detalle/?kword=' + kword)
//          .then(function(response){
//            self.lista_opciones = response.data
//          })
//          .catch( function(error){
//            console.log(error);
//          })

//       },

//       AgregarOpcion: function(opcion){
//         this.lista_agregados.push(opcion);
//         // this.newmasdetalles='';
//       },

//       RegistrarMasDetalle: function(){
        
//         var lista_mas_detalle = []
//         for (let i = 0; i < this.lista_agregados.length; i++){
//           lista_mas_detalle.push(this.lista_agregados[i].id)
//         }
        
//         var data_mas_detalles = {
//           'detalle_observaciones': lista_mas_detalle,
//         }
//         var self = this;
//         axios.post('/recepcionmp/api/registra_mas_detalle/', data_mas_detalles )
//          .then(function(response){
//           self.mensaje = 'Almacenado!'
           
//          })
//          .catch( function(error){
//            console.log(error);
//          })

//       }

//     },
    
//   }).mount('#observa');