import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";
/* import "../../styles/login.css";
 */

export const LoginAdmin = () => {
    const { store, actions } = useContext(Context);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [viewPassword, setViewPassword] = useState(false)
    const navigate = useNavigate();
  

    function handleEmail(event) {
      setEmail(event.target.value)
    }

    const handlePassword = (event) => {
      setPassword(event.target.value)
    }
  
    const handleReset = () => {
      setEmail('');
      setPassword('');
    }
  
    const handleViewPassword = () => setViewPassword(!viewPassword)
  
    const handleSumbit = (event) => {
      event.preventDefault();
      const dataToSend = {
        email: email,
        password: password
      }
      actions.loginAdmin(dataToSend)
      handleReset()
      navigate('/')
    }
  


    return (
    <> 
   
     <div className="login-container card-body">
      <h2>Staff login</h2>
      <form onSubmit={handleSumbit}>
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label red-color">Email: </label>
          <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
            value={email} onChange={handleEmail} /> 
          <div id="emailHelp" className="form-text"></div>
        </div>

        <div className="mb-3">
          <label htmlFor="exampleInputPassword1" className="form-label red-color">Password:</label>
          <div className="input-group">
            <input type={viewPassword ? "text" : "password"} className="form-control" id="exampleInputPassword1" aria-describedby="passwordHelp"
              value={password} onChange={handlePassword} />
            <span className="input-group-text fs-6" onClick={handleViewPassword}>
              {viewPassword ? <i className="far fa-eye-slash"></i> : <i className="far fa-eye"></i>}
            </span>
          </div>
            <div id="passwordHelp" className="form-text"><Link to="/signup"></Link></div>
        </div>

        <button type="submit" className="btn-custom red-background">Enviar</button>
        <button type="reset" className="btn-custom btn-secondary ms-3 mt-3"
          onClick={handleReset}> Borrar
        </button>
      </form>
      </div>
    </>
    )
}