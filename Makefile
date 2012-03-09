all: gitosis

gitosis:
	./prepare.sh

clean:
	userdel git
	rm -rf /home/git
