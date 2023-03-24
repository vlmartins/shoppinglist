import { useNavigate, Link } from "react-router-dom";


export default function ProjectShoppingList() {
    return (
        <div>
            <p>
                <span className='red'>Project 1 - </span> 
                <span className='green'> Shopping List - </span>
                <span className='yellow'> <a href="https://github.com/" target="_blank" title="Go to my Git repo">View Code</a> - 
                  </span> 
                <span className='light_blue'> <Link to="/SignUp">Register</Link> - 
                <Link to="/Login"> Sign In </Link> </span>
            </p>    
        </div>
    )

}