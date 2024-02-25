import React, { useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import { showErrorPage } from '../../utils/errors';
import axios from 'axios';
import { urls } from '../../utils/constants';
import Alert from '@mui/material/Alert';

function LoginPage() {
  const requiredSearchParams = ['client_id', 'redirect_uri'];
  const [searchParams] = useSearchParams();
  for (let searchParam of requiredSearchParams) {
    if (!searchParams.has(searchParam)) {
      showErrorPage(400);
      break;
    }
  }

  const [error, setError] = useState('');
  const [email, setEmail] = useState('');
  const [loading, setIsLoading] = useState(false);

  const [password, setPassword] = useState('');
  const handleSubmit = async (e) => {
    setIsLoading(true);
    e.preventDefault();
    const response = await axios.post(urls.api.login, {
      email: email,
      password: password,
      client_id: searchParams.get('client_id')
    });
    const {success, code, reason} = response.data;
    if (response.status === 200 && success) {
      window.location.assign(
        `${searchParams.get('redirect_uri')}?code=${code}`
      );
      return;
    }
    setError(reason);
    setIsLoading(false);
  };

  return (
    <div className="bg-slate-900 flex justify-center items-center h-screen font-mono">
      <div className="dark:bg-slate-800 p-8 rounded-lg w-96 border border-slate-500 border-1">
        <form className="space-y-4" onSubmit={handleSubmit}>
          <h2 className='text-2xl text-white text-center font-thin'>Welcome to <span className='text-blue-800 font-bold font'>Lakelon.dev</span></h2>
          <div>
            <label htmlFor="email" className="block text-sm font-medium text-slate-200">Email</label>
            <input
              type="email"
              id="email"
              name="email"
              required
              className="mt-1 p-2 w-full bg-black text-white rounded-md shadow-lg"
              value={email}
              onFocus={() => setError('')}
              onChange={(e) => {
                setError('')
                setEmail(e.target.value);
              }}
            />
          </div>
          <div>
            <label htmlFor="password" className="block text-sm font-medium text-slate-200">Password</label>
            <input
              type="password"
              id="password"
              name="password"
              required
              className="mt-1 p-2 w-full bg-black text-white rounded-md shadow-lg"
              value={password}
              onFocus={() => setError('')}
              onChange={(e) => {
                setError('')
                setPassword(e.target.value);
              }}
            />
          </div>
          <div>
            <button type="submit" className="w-full transition-all border flex justify-center border-slate-500 text-white p-2 rounded-md hover:bg-black hover:border-gray-700">
              {loading
              ? (
                <svg aria-hidden="true" className="w-6 h-6 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                  <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
              </svg>
              )
              : 'Access'
              }
              </button>
          </div>
          {error && (
            <Alert severity='error'>{error}</Alert>
          )}
        </form>
      </div>
    </div>
  );
}

export default LoginPage;
