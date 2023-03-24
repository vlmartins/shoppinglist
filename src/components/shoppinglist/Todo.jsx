import React from 'react'
import "../../sass/shoppinglist.sass"
import axios from '../../api/axios';


function TodoItem(props) {

    const DELETE_URL = "/api/todo/"

    const deleteTodoHandler = (_id) => {
    axios.delete(`${DELETE_URL}${_id}`, {withCredentials: true})
        .then(res => console.log(res.data)) }
  
    return (
        <div class="todo">
            <p>
                <span> {props.todo.desc}  </span>
                <button onClick={() => deleteTodoHandler(props.todo._id)}  >X</button>
            </p>
        </div>
    )
}

export default TodoItem;