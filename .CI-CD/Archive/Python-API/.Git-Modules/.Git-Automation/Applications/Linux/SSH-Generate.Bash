#!/bin/bash --posix

# -*- Coding: UTF-8 -*- #
# -*- System: Linux -*- #
# -*- Usage:   *.*  -*- #

tput civis

Elevation () {
	if [[ "${UID}" == "0" ]]; then
		echo "User !:= root"
		exit -1
	fi
    if [ -n "${SUDO_USER}" ]; then
		echo "User !:= Sudo"
        exit -1
    fi
}; Elevation

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

if [ ! -n "${1}" ]; then
	echo "A Key-Name is Required as Input (1)" && exit -1
else
	KEYNAME="${1}"
fi
if [ ! -n "${2}" ]; then
	echo "An AWS Profile is Required as Input (2)" && exit -1
else
	PROFILE="${2}"
fi

if [ -f "${CWD}/${KEYNAME}" ]; then
	printf "%s" "Delete Previous Key-Pair? (Y/N): "
	tput cnorm && tput cvvis && read RESPONSE
	tput civis
	if [[ $RESPONSE == "y" ]] || [[ $RESPONSE == "Y" ]] \
		|| [[ $RESPONSE == "yes" ]] || [[ $RESPONSE == "Yes" ]]; then
		rm -f "${CWD}/${KEYNAME}"
		rm -f "${CWD}/${KEYNAME}.pub"
	else
		echo "Please Handle the Import-Key Process Accordingly" \
			&& exit 0
	fi
fi

ssh-keygen -b 2048 -t RSA -f "${CWD}/${KEYNAME}" -C "$(uuidgen)" -N ""

Loader=(
"▐●          ▌"
"▐ ●         ▌"
"▐  ●        ▌"
"▐   ●       ▌"
"▐    ●      ▌"
"▐      ●    ▌"
"▐       ●   ▌"
"▐        ●  ▌"
"▐         ● ▌"
"▐          ●▌"
"▐         ● ▌"
"▐        ●  ▌"
"▐       ●   ▌"
"▐      ●    ▌"
"▐     ●     ▌"
"▐    ●      ▌"
"▐   ●       ▌"
"▐  ●        ▌"
"▐ ●         ▌")

(aws ec2 describe-key-pairs \
	--key-names "${KEYNAME}" \
	--profile "${PROFILE}") 1>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
PID=$!
while ps -p $PID &>/dev/null; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done

done
trap - EXIT

if [[ "$(cat ${TMPDIR}/output.log)" != "" ]]; then
	printf "%s" "Overwrite Previous Import? (Y/N): "
	tput cnorm && tput cvvis && read RESPONSE
	tput civis
	if [[ $RESPONSE == "y" ]] || [[ $RESPONSE == "Y" ]] \
		|| [[ $RESPONSE == "yes" ]] || [[ $RESPONSE == "Yes" ]]; then
		aws ec2 delete-key-pair --key-name "${KEYNAME}" --profile "${PROFILE}" &
		PID=$!; trap "kill $PID 2>/dev/null" EXIT
		while ps -p $PID 1>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log; do
		    for ((i = 0; i < ${#Loader[@]}; i++)); do
				printf "${Loader[$i]}\r"
				sleep 0.185
			done
		done
		trap - EXIT
		if [[ "$(cat ${TMPDIR}/output-err.log)" == "" ]]; then
			(rm -r -f "${TMPDIR}/output-err.log") \
				2>/dev/null 1>&2
			(rm -r -f "${TMPDIR}/output.log") \
				2>/dev/null 1>&2
		else
			cat ${TMPDIR}/output-err.log && exit -1
		fi
	else
		echo "Please Handle the Import-Key Process Accordingly" \
			&& exit 0
	fi
fi
(aws ec2 import-key-pair \
    --key-name "${KEYNAME}" \
    --public-key-material "fileb://${CWD}/${KEYNAME}.pub" \
	--profile "${PROFILE}") 1>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &

PID=$!
while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done

done
trap - EXIT

(aws ssm get-parameter \
	--name "${KEYNAME}" \
	--profile "${PROFILE}") 1>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
PID=$!
while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done

done
trap - EXIT
echo "Checked SSM Parameter (1/3) [${KEYNAME}]"
(aws ssm get-parameter \
	--name "${KEYNAME}-Key-Private" \
	--profile "${PROFILE}") 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log &
PID=$!
while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done
done
trap - EXIT
echo "Checked SSM Parameter (2/3) [${KEYNAME}-Key-Private]"
(aws ssm get-parameter \
	--name "${KEYNAME}-Key-Public" \
	--profile "${PROFILE}") 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log &
PID=$!
while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
    for ((i = 0; i < ${#Loader[@]}; i++)); do
        printf "${Loader[$i]}\r"
        sleep 0.185
    done
done
trap - EXIT
echo "Checked SSM Parameter (3/3) [${KEYNAME}-Key-Public]"

if [[ "$(cat ${TMPDIR}/output.log)" != "" ]]; then
	printf "%s" "Overwrite Previous SSM Imports? (Y/N): "
	tput cnorm && tput cvvis && read RESPONSE
	tput civis
	if [[ $RESPONSE == "y" ]] || [[ $RESPONSE == "Y" ]] \
		|| [[ $RESPONSE == "yes" ]] || [[ $RESPONSE == "Yes" ]]; then
		(aws ssm put-parameter \
			--name "${KEYNAME}" \
			--type "String" \
			--tier "Standard" \
			--value "${KEYNAME}" \
			--overwrite \
			--profile "${PROFILE}")1>${TMPDIR}/output.log2>${TMPDIR}/output-err.log &
		PID=$!
		while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
			for ((i = 0; i < ${#Loader[@]}; i++)); do
				printf "${Loader[$i]}\r"
				sleep 0.185
			done
		done
		trap - EXIT
		echo "Successful Import (1/3) [${KEYNAME}]"
		(aws ssm put-parameter \
			--name "${KEYNAME}-Key-Private" \
			--type "String" \
			--tier "Standard" \
			--value "$(cat ${CWD}/${KEYNAME})" \
			--overwrite \
			--profile "${PROFILE}")>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
		PID=$!
		while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
			for ((i = 0; i < ${#Loader[@]}; i++)); do
				printf "${Loader[$i]}\r"
				sleep 0.185
			done
		done
		trap - EXIT
		echo "Successful Import (2/3) [${KEYNAME}-Key-Private]"
		(aws ssm put-parameter \
			--name "${KEYNAME}-Key-Public" \
			--type "String" \
			--tier "Standard" \
			--value "$(cat ${CWD}/${KEYNAME}.pub)" \
			--overwrite \
			--profile "${PROFILE}")>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
		PID=$!
		while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
			for ((i = 0; i < ${#Loader[@]}; i++)); do
				printf "${Loader[$i]}\r"
				sleep 0.185
			done
		done
		trap - EXIT
		echo "Successful Import (3/3) [${KEYNAME}-Key-Public]"
	else
		echo "Please Handle the Import-Key Process Accordingly" \
			&& exit 0
	fi
else
	(aws ssm put-parameter \
		--name "${KEYNAME}" \
		--type "String" \
		--tier "Standard" \
		--value "${KEYNAME}" \
		--profile "${PROFILE}")>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
	PID=$!
	while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
		for ((i = 0; i < ${#Loader[@]}; i++)); do
			printf "${Loader[$i]}\r"
			sleep 0.185
		done
	done
	trap - EXIT
	echo "Successful Import (1/3) [${KEYNAME}]"
	(aws ssm put-parameter \
		--name "${KEYNAME}-Key-Private" \
		--type "String" \
		--tier "Standard" \
		--value "$(cat ${CWD}/${KEYNAME})" \
		--profile "${PROFILE}")>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
	PID=$!
	while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
		for ((i = 0; i < ${#Loader[@]}; i++)); do
			printf "${Loader[$i]}\r"
			sleep 0.185
		done
	done
	trap - EXIT
	echo "Successful Import (2/3) [${KEYNAME}-Key-Private]"
	(aws ssm put-parameter \
		--name "${KEYNAME}-Key-Public" \
		--type "String" \
		--tier "Standard" \
		--value "$(cat ${CWD}/${KEYNAME}.pub)" \
		--profile "${PROFILE}")>${TMPDIR}/output.log 2>${TMPDIR}/output-err.log &
	PID=$!
	while kill -0 $PID 1>>${TMPDIR}/output.log 2>>${TMPDIR}/output-err.log; do
		for ((i = 0; i < ${#Loader[@]}; i++)); do
			printf "${Loader[$i]}\r"
			sleep 0.185
		done
	done
	trap - EXIT
	echo "Successful Import (3/3) [${KEYNAME}-Key-Public]"
fi

rm $TMPDIR/output*

printf "%s" "Move SSH Resources to .SSH Directory? (Y\N): "
tput cnorm && tput cvvis && read RESPONSE
tput civis
if [[ $RESPONSE == "y" ]] || [[ $RESPONSE == "Y" ]] \
	|| [[ $RESPONSE == "yes" ]] || [[ $RESPONSE == "Yes" ]]; then
	mv "${CWD}/${KEYNAME}" "${HOME}/.ssh"
	mv "${CWD}/${KEYNAME}.pub" "${HOME}/.ssh"
fi

tput cnorm && tput cvvis

printf "%s\n" "SSH Management Process Complete" && exit 0
