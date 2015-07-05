# Clearbit + Slack + Flask

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## This is an api for alerting your team when your app gains a new customer.

![sample of what you would see](https://www.dropbox.com/s/4kte9bc1ubfal07/Screenshot%202015-07-05%2018.03.44.png?dl=0)

## Installation Instructions

```
1. Click the 1-click deploy to heroku
2. Add your Clearbit Key and Slack Key as Heroku Config Vars 'CLEARBIT' and 'SLACK'
3. Add a line of code to your app which passes an email to this api
4. See the result in slack
``` 

## Usage

```
$http.get('some-clever-name.herokuapp.com/' + email)
  .then(function(result) {
    // sweet you got a new customer!
});
```

## Todo

1. Add security so anyone can't hit your endpoint.

## Contributing

1. Fork it ( https://github.com/[my-github-username]/clearbit-slack/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request