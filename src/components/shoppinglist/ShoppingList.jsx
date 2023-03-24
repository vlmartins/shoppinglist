import "../../sass/shoppinglist.sass"
import axios from '../../api/axios';
import React, { useState, useEffect} from 'react'
import TodoView from './TodoListView'
import Footer from './Footer'


function ShoppingList() {
  const POST_URL = '/api/todo/'
  const GET_URL = '/users/me/items/'
 

  const [todoList, setTodoList] = useState([])
  const [desc, setDesc] = useState('')
  const [count, setCount] = useState(0)


  async function handleIncrement() {
    await setCount(count + 1);
  };

  function addTodoHandler() {
    axios.post(POST_URL, { 'desc': desc },
    {withCredentials: true}
    )
      .then(res => console.log(res),handleIncrement())
      .catch(res => console.log(res));
  };

  function cadastrar(event) {
    event.preventDefault()
    addTodoHandler
    const resetform = document.getElementById("form");
    resetform.reset();
    setDesc('');
    
  }

useEffect(() => {
  const timer = setTimeout(() => {
  axios.get(GET_URL,
    {withCredentials: true})
    .then(res => {setTodoList(res.data),handleIncrement();})
  }, 450);
  return () => clearTimeout(timer);
  },[count]);
  
  return (
    <div className="App1"  >
      <nav id="nav"> Shopping List </nav>
      <div>
        <p></p>
        <form className="forms2" id="form" onSubmit={cadastrar} >
          <div className="form-group">  
              <input type="text" class="form-field"   onChange={event => setDesc(event.target.value)}  placeholder='Item'/>
              <button  onClick={addTodoHandler}>  Save</button>         
          </div> 
        </form>
        <div>
          <TodoView  todoList={todoList} />
        </div>
      </div>
      <Footer count={count} />
    </div>
  )
}


export default ShoppingList