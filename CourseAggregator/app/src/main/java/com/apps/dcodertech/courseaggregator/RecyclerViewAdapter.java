package com.apps.dcodertech.courseaggregator;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import butterknife.BindView;
import butterknife.ButterKnife;


import java.util.List;

/**
 * Created by dhruv on 2/6/2018.
 */

public class RecyclerViewAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> implements View.OnClickListener {
    private Context context;
    private List<Courses> courses;
    private CustomItemClickListener listener;
    public RecyclerViewAdapter(List<Courses> list, CustomItemClickListener customItemClickListener) {
        courses = list;
        listener = customItemClickListener;
    }
    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.list_card, parent, false);
        final MyViewHolder holder = new MyViewHolder(v);
        //implementing the onItemClickListener using the interface class created
        v.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View mv) {
                listener.onItemClick(mv, holder.getAdapterPosition());
            }
        });
        return holder;
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {
        Courses b = courses.get(position);
        ((MyViewHolder) holder).titleTextView.setText(b.getTitle());
        ((MyViewHolder) holder).authorTextView.setText(b.getTeacher());
        ((MyViewHolder) holder).certificationView.setText(b.getCertificates());
        ((MyViewHolder) holder).courseProvider.setText(b.getProvider());
        ((MyViewHolder) holder).universityProvider.setText(b.getInstitution());
        ((MyViewHolder) holder).hoursView.setText(b.getHours());
        ((MyViewHolder) holder).weeksView.setText(b.getDuration());

    }

    @Override
    public int getItemCount() {
        return null != courses ? courses.size() : 0;
    }

    @Override
    public void onClick(View v) {

    }
    public class MyViewHolder extends RecyclerView.ViewHolder {
        @BindView(R.id.title)
        public TextView titleTextView;
        @BindView(R.id.authorsView)
        TextView authorTextView;
        @BindView(R.id.certificationView)
        TextView certificationView;
        @BindView(R.id.universityProvider)
        TextView universityProvider;
        @BindView(R.id.courseProvider)
        TextView courseProvider;
        @BindView(R.id.weeksView)
        TextView weeksView;
        @BindView(R.id.hoursView)
        TextView hoursView;

        public MyViewHolder(View itemView) {
            super(itemView);
            ButterKnife.bind(this, itemView);
        }
    }
}
