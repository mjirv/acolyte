module.exports = {
    devServer: {
        proxy: {
            '^/api': {
                //target: 'http://localhost:5000',
                target: 'https://acolyte-api.herokuapp.com',
                changeOrigin: true
            }
        }
    } 
}