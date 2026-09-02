
Take secrets from a pipe?
<https://smallstep.com/blog/command-line-secrets/>

IMSD = Instance Metadata Service. HTTP endpoint.  From within the VM it's reachable at the fixed address http://169.254.169.254;
that's a link-local IP that never routes anywhere,
so only processes on the VM itself can reach it, and the traffic never touches a real network.
