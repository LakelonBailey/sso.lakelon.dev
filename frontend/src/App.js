import './App.css';
import './output.css';
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import LoginPage from './pages/Login';
import Error from './pages/Error';

function App(){
 return (
  <BrowserRouter>
    <Routes>
       <Route exact path="/" element={<LoginPage />}></Route>
       <Route exact path="/error/:errorCode" element={<Error />}></Route>
       <Route path="*" element={<Navigate to="/error/404" replace />} />
    </Routes>
  </BrowserRouter>
 );
}

export default App;