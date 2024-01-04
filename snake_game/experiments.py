
# First try using list for repositioning

# def get_positions_of_all_segments(snake_segments_list):
#     """Enter a list with snake segments and return their position in form of a list"""
#     snake_segments_positions_list = []
#     for snake_segment in snake_segments_list:
#         snake_segments_positions_list.append(snake_segment.position())
#     return snake_segments_positions_list

# def snake_move_forward(snake_segments_list):
#     snake_segments_positions_list = get_positions_of_all_segments(snake_segments_list)
#     for i, snake_segment in enumerate(snake_segments_list):
#         if i == 0:
#             snake_segment.forward(20)
#             snake_segments_positions_list.insert(0,snake_segment.position())
#         else:
#             snake_segment.goto(snake_segments_positions_list[i])

# def snake_move_left(snake_segments_list):
#     snake_segments_positions_list = get_positions_of_all_segments(snake_segments_list)
#     for i, snake_segment in enumerate(snake_segments_list):
#         if i == 0:
#             snake_segment.left(90)m
#             snake_segment.forward(20)
#             snake_segments_positions_list.insert(0,snake_segment.position())
#         else:
#             snake_segment.goto(snake_segments_positions_list[i])

# def snake_move_right(snake_segments_list):
#     snake_segments_positions_list = get_positions_of_all_segments(snake_segments_list)
#     for i, snake_segment in enumerate(snake_segments_list):
#         if i == 0:
#             snake_segment.right(90)
#             snake_segment.forward(20)
#             snake_segments_positions_list.insert(0,snake_segment.position())
#         else:
#             snake_segment.goto(snake_segments_positions_list[i])