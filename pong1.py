
import simplegui

width=600
height=400
paddle1_vel=0
paddle2_vel=0
pad_width=8
pad_height=80
paddle1_pos=height/2
paddle2_pos=height/2
half_pad_height=pad_height/2
ball_pos=[width/2,height/2]
ball_vel=[4,2]
radius=20
score=0
score1=0





def keydown(key):
    global paddle1_vel,paddle2_vel
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel=-4
    if key==simplegui.KEY_MAP['down']:
        paddle2_vel=+4
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel=-4
    if key==simplegui.KEY_MAP['s']:
        paddle1_vel=+4 
        
        
        
def keyup(key):
    global paddle1_vel,paddle2_vel
    if key==simplegui.KEY_MAP['up']:
        paddle2_vel=0
    if key==simplegui.KEY_MAP['down']:
        paddle2_vel=0
    if key==simplegui.KEY_MAP['w']:
        paddle1_vel=0
    if key==simplegui.KEY_MAP['s']:
        paddle1_vel=0
        
        
def draw(canvas):
    global paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel,height,half_pad_height,pad_width,ball_pos,radius,ball_vel,score,score1
    if paddle1_pos<=half_pad_height and paddle1_vel<0:
        paddle1_vel=0
    if paddle1_pos>=(height-half_pad_height) and paddle1_vel>0:
        paddle1_vel=0
    if paddle2_pos<=half_pad_height and paddle2_vel<0:
        paddle2_vel=0
    if paddle2_pos>=(height-half_pad_height) and paddle2_vel>0:
        paddle2_vel=0
    
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    
    if ball_pos[0]<=radius+pad_width:
        ball_vel[0]=-ball_vel[0]
        
    #if ball_pos<(paddle1_pos+half_pad_height) and ball_pos[1]>(paddle1_pos-half_pad_height):
    #    if ball_pos[0]<=radius+pad_width:
    #       ball_vel[0]=-ball_vel[0]
        
        
    if ball_pos[0]>=width-radius-pad_width:
        ball_vel[0]=-ball_vel[0]
    
    if ball_pos[1]<=radius:
        ball_vel[1]=-ball_vel[1]
    if ball_pos[1]>=height-radius:
        ball_vel[1]=-ball_vel[1]
        
    if ball_pos[0]<=radius+pad_width:
        ball_pos[0]=ball_pos[0]+(width/2)
        ball_vel[0]=-ball_vel[0]
        score1=score1+1
    if ball_pos[0]>=width-radius-pad_width:
        ball_pos[0]=ball_pos[0]-(width/2)
        ball_vel[0]=-ball_vel[0]
        score=score+1

        
        
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    
    
    
    
    
    
    canvas.draw_polygon([(0, paddle1_pos-half_pad_height), (0, paddle1_pos+half_pad_height), (pad_width+3, paddle1_pos+half_pad_height),(pad_width+3,paddle1_pos-half_pad_height)], pad_width-1, "White","White")
    canvas.draw_polygon([(width, paddle2_pos-half_pad_height), (width, paddle2_pos+half_pad_height), (width-pad_width-3, paddle2_pos+half_pad_height),(width-pad_width-3,paddle2_pos-half_pad_height)], pad_width-1, "White","White")
    canvas.draw_line([width/2,0],[width/2,height],1,'white')
    canvas.draw_line([pad_width,0],[pad_width,height],1,'white')
    canvas.draw_line([width-pad_width,0],[width-pad_width,height],1,'white')
    canvas.draw_circle(ball_pos,radius,2,'red','white')
    canvas.draw_text(str(score),(400,200),50,'red')
    canvas.draw_text(str(score1),(200,200),50,'red')
    
    
frame=simplegui.create_frame('pong',width,height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.start()
    
    
    
        
        
               
    
