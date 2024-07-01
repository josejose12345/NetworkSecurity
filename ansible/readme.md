# Network Security with Ansible

I am following [this tutorial](https://www.youtube.com/watch?v=MNGfPn0Yvs8&list=PLiH9_MU-6RjLIUCbpJv2xZc9zwLPkdyOY&index=10&ab_channel=Pythoholic)

Firstly, I deployed the following AWS simple architecture of 3 EC2 instances, with one ansible host:
![AWS Architecture](aws_ec2.png)

Then a ping was tested using SSH from the host to both target instances:

```
ssh-agent bash
cp ec2-key.pem ~/.ssh/
ssh-add ~/.ssh/ec2-key.pem
```

![Ping Connection](ping_connection.png)

![Network Security](https://example.com/network-security.png)
