MODEL="gpt-4o" # your engine name: gpt-4o, gpt35-turbo, gpt-4o-mini, o1-mini
MODEL_TYPE="gpt" # 'gpt'

DATA_FILE="logic_grid_puzzle_200.jsonl"

START_IDX=0
END_IDX=200

# choose method
METHOD="bpp" # ["standard", "cot", "self_refine", "spp", "bpp", "macro_bpp", "meso_bpp", "micro_bpp", "bpp_w_r_demo", "bpp_w_k_demo", "bpp_two_k_demo", "bpp_two_r_demo"]

# w/ or w/o system message (BPP works without a system message, but you can add one if you want)
SYSTEM_MESSAGE="" # or "You are an AI assistant that helps people find information."

python run.py \
    --model ${MODEL} \
    --model_type ${MODEL_TYPE} \
    --method ${METHOD} \
    --task logic_grid_puzzle \
    --task_data_file ${DATA_FILE} \
    --task_start_index ${START_IDX} \
    --task_end_index ${END_IDX} \
    --system_message "${SYSTEM_MESSAGE}" \
    ${@}

