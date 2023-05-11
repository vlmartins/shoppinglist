import { Outlet } from "react-router-dom"
import ProjectShoppingList from '../components/ProjectShoppingList'
import Login from  '../components/Login.jsx'
import About from '../components/About.jsx'


const Layout = () => {
    return (
        <div className="Layout">
            <Outlet />
            <About />
            <ProjectShoppingList />
        </div>
    )
}

export default Layout
