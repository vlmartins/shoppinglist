import { useState } from 'react'
import axios from './api/axios';
import TodoView from './components/shoppinglist/TodoListView.jsx';
import React, {useEffect} from 'react'


class MyComponent extends React.Component {
  constructor(props) {
    super(props);
    this.handleIncrement = this.handleIncrement.bind(this);
    this.addTodoHandler = this.addTodoHandler.bind(this);
  }
}


function test() {
  const LOGIN_URL = '/sign_in';
  const [user, setUser] = useState("")
  const [password, setPassword] = useState("")
  const READ_ITEMS = "/users/me/items/";
  const local_post = 'http://localhost:3500/api/todo/'
  const local_get = 'http://localhost:3500/users/me/items/'
  const [getAdress] = useState(local_get)
  const [postAdress] = useState(local_post)
  const [todoList, setTodoList] = useState([])
  const [desc, setDesc] = useState('')
  const [count, setCount] = useState(0)
  const handleToken = async (e) => {
    e.preventDefault();
    try {
        const response = await axios.post(LOGIN_URL,
            {
              username: user,
              password: password
            },
            {
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                withCredentials: true
            }
        );
        console.log(JSON.stringify(response?.data));
  } catch (err) { console.log(err)
}}


const readItems= async () => {
 
  try {
      const response = await axios.get(READ_ITEMS,
          {

              headers: { 'accept': 'application/json' },
              withCredentials: true
          }
      );
      console.log(JSON.stringify(response?.data));
} catch (err) { console.log(err)
}}

async function handleIncrement() {
  await setCount(count + 1);
};

function addTodoHandler() {
  axios.post(postAdress, { 'desc': desc },
  {withCredentials: true}
  )
    .then(res => console.log(res),handleIncrement())
    .catch(res => console.log(res));
};

function cadastrar(event) {
  event.preventDefault()
  addTodoHandler
  const resetform = document.getElementById("forms");
  resetform.reset();
  setDesc('');
}

  useEffect(() => {
    const timer = setTimeout(() => {
    axios.get(getAdress, 
      {withCredentials: true})
      .then(res => {setTodoList(res.data),handleIncrement();})
    }, 5000);
    return () => clearTimeout(timer);
    },[count]);
  


  return (
    <div >
      <h1> hi</h1>
      <form onSubmit={handleToken}>
        <input onChange={event => setUser(event.target.value)} placeholder="user"></input>
        <input  onChange={event => setPassword(event.target.value)} placeholder="password"></input>
        <br></br>
        <button> /sign_in Get Token</button>
      </form>
      <br></br>
      <button onClick= {readItems}> Read Items</button>
      <br></br>
      <form id="forms"  onSubmit={cadastrar} >
          <div class="form-group">  
              <input type="text" class="form-field"   onChange={event => setDesc(event.target.value)}  placeholder='Compra'/>
              <button  onClick={addTodoHandler}>  Salvar</button>         
          </div> 
        </form>
        <TodoView  todoList={todoList} />

    </div>
  )
}

export default test