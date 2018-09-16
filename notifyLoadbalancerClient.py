import grpc
import subprocess

import NotifyLoadBalancer_pb2
import NotifyLoadBalancer_pb2_grpc

def notifyLoadBalancer():
	instance_id = subprocess.check_output('wget -q -O - http://169.254.169.254/latest/meta-data/instance-id',stderr=subprocess.STDOUT,shell =True)
	instance_dns = subprocess.check_output('wget -q -O - http://169.254.169.254/latest/meta-data/public-hostname',stderr=subprocess.STDOUT,shell =True)
	# channel = grpc.insecurimport subprocesssubpe_channel('localhost:50051')
	# stub = NotifyLoadBalancer_pb2_grpc.NotifyLoadBalancerStub(channel)
	# response = stub.AddInstance(NotifyLoadBalancer_pb2.Instance(instance_id = instance_id,instance_dns = instance_dns))
	print("Paramters being passed are " ,instance_id)
	print("Paramters being passed are " ,instance_dns)
	# channel.close()

if __name__ == '__main__':
    notifyLoadBalancer()