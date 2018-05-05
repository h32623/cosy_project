var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/Login', function(req, res){
  res.render('Login.ejs');
});

router.get('/RegPage', function(req, res){
  res.render('RegPage.ejs');
});

router.get('/ActivePage', function(req, res){
    res.render('ActivePage.ejs');
});


router.get('/RegPageUI', function(req, res){
    res.render('RegPageUI.ejs');
});

router.get('/ActivePageUI', function(req, res){
    res.render('ActivePageUI.ejs');
});

router.get('/ChatPage', function(req, res){
    res.render('ChatPage.ejs');
});

router.get('/devcamp', function(req, res){
    res.render('devcamp.ejs');
});

module.exports = router;
