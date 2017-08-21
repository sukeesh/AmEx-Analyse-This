import network
import leaderboard
import amex_loader

# print "Loading leader board data"
# leader_board_data = leaderboard.load_data_wrapper()
# print "Done"

print "Loading training and test data"
training_data, test_data = amex_loader.load_data_wrapper()
print "Done"

accuracy = 0.0
hidden_neurons = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
config = 0

for it in hidden_neurons:
	# print it
	net = network.Network([43, it, it - 2, 3])
	here_acc = net.SGD(training_data, 2000, 500, test_data=test_data)
	# print here_acc
	if here_acc > accuracy:
		here_acc = accuracy
		config = it

print config

# print "Training data"

# print "Printing Leader board!"
# net.leader_print(leader_board_data)
# print "Successful!"