<template>
    

    

<div class="container-fluid"> 
        <h2 class="alert alert-danger mt-2">Technical Test</h2>

        <div class="row">

            


            <div class="col-md-7">


                <h2 class="alert alert-success">List of Movies</h2>

                <table class="table table-bordered mt-4">
  <thead>
    <tr>
      <th scope="col">Name</th>
      <th scope="col">Description</th>
      <th scope="col">Price</th>
      <th scope="col">Image</th>
      <th scope="col">Category</th>
      <th scope="col">Action</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="movie in movies" >
        <td>{{movie.name}}</td>
      <td>{{movie.description}}</td>
      <td>{{movie.price}}</td>
      <td>{{movie.image}}</td>
      <td>{{movie.category}}</td>
      <td>
        <a href="#" class="edit" title="" ><button @click="editBtn(movie.id)" class="btn btn-warning btn-sm">Edit</button></a>
        <a href="#" class="edit ml-1" title="" ><button @click="deleteMovie(movie.id)"  class="btn btn-danger btn-sm">Delete</button></a>


      </td>
    </tr>
  </tbody>
</table>

            </div>


            <div class="col-md-5">



                  <!-- There is a current movie to be edited -->

                <div v-if="Object.keys(this.currentMovie).length !== 0" >
                

                    <h2 class="alert alert-warning">Edit Movie Details</h2>

                    <form @submit.prevent="editMovie(this.currentMovie.id)">

<div class="row">

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Name</label>
<input type="text" class="form-control" v-model="currentMovie.name" >
</div>
    </div>

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Description</label>
<input type="text" class="form-control" v-model="currentMovie.description">
</div>
    </div>
</div>



<div class="row">
    <div class="col">
        <div class="form-group">
        <label class="form-label float-left ml-2">Price</label>
        <input type="text" class="form-control" v-model="currentMovie.price">
        </div>
    </div>

    <div class="col">

    <div class="form-group">
    <label class="form-label float-left ml-2">Category</label>
    <input type="text" class="form-control" v-model="currentMovie.category">
    </div>
</div>

<div class="row">
    <div class="col">
        <div class="form-group">
        <label class="form-label float-left ml-2">Image</label>
        <input type="text" class="form-control" v-model="currentMovie.image">
        </div>
    </div>

    
</div>



</div>
<button type="submit" class="btn btn-success float-left ml-2">Update</button>
</form>

                </div>




                <!-- There is no current movie to be edited -->

                <div v-else  >
                    <h2 class="alert alert-info">Create A New Movie</h2>
                    <form @submit.prevent="saveMovie()">

<div class="row">

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Name</label>
<input type="text" class="form-control" v-model="movie.name">
</div>
    </div>

    <div class="col">
        <div class="form-group">
<label class="form-label float-left ml-2">Description</label>
<input type="text" class="form-control" v-model="movie.description">
</div>
    </div>
</div>



<div class="row">

<div class="col">
<div class="form-group">
<label class="form-label float-left ml-2">Price</label>
<input type="text" class="form-control" v-model="movie.price">
</div>
</div>
<div class="col">

<div class="form-group">
<label class="form-label float-left ml-2">Category</label>
<input type="text" class="form-control" v-model="movie.category">
</div>
</div>

</div>

<div class="row">
    
    <div class="col">
    <div class="form-group">
    <label class="form-label float-left ml-2">Image</label>
    <input type="text" class="form-control" v-model="movie.image">
    </div>
    </div>
    
    
</div>


<button type="submit" class="btn btn-primary float-left ml-2">Save</button>
</form>
                </div>
            </div>
        </div>
    </div>





</template>



<script>
import axios from 'axios'

export default{
    data(){
        return {
            'api': 'http://localhost:5000/api/movies/',
            movies: [],
            currentMovie: {},
            'movie': {
                'name': '',
                'description': '',
                'price': '',
                'image': '',
                'category': '',
            }

        }
    },

    

    mounted(){
        console.log('DOM mounted')
    },


    created(){
        console.log('DOM created')
        this.getMovies()
    },



    methods: {

        getMovies(){
            axios.get(this.api).then(
                response => { 
                    console.log(response.data.movies)
                    this.movies = response.data.movies
                    
        }
      )
    },

    saveMovie(){
            axios.post(this.api, this.movie).then(
                response => { 
                    console.log(response.data)
                    this.movie = {}
                    this.getMovies()
                }
            )

        },

        editBtn(id){
            console.log(id)
            this.movies.map(movie => {
                if(movie.id === id){
                    console.log(movie.name)
                    this.currentMovie = {'id':movie.id, 'name':movie.name, 'description':movie.description, 'price':movie.price, 'image':movie.image, 'category':movie.category}
                }
            })


        },
        
        editMovie(){
            axios.put(this.api, this.currentMovie).then(
                response => { 
                    console.log(response.data)
                    this.currentMovie = {}
                    this.getMovies()
                }
            )

        },

        deleteMovie(id){

          axios.patch(this.api, {'id':id}).then(
          response => { 
          console.log(response.data)
          this.getMovies()
    }
)

},



    },




    
}

</script>