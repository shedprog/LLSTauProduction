GET_XSEC() {
    case $1 in
        50)  echo "5.368" ;;
        100) echo "0.3657" ;;
        150) echo "0.08712" ;;
        200) echo "0.03031" ;;
        250) echo "0.01292" ;;
        300) echo "0.006254" ;;
        350) echo "0.002931" ;;
        400) echo "0.001859" ;;
        450) echo "0.001216" ;;
        500) echo "0.0006736" ;;
        *) printf '%s\n' "Error: Unknown Stau Mass"  1>&2; exit 1 ;;
    esac
}