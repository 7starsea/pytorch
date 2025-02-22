#pragma once

#ifdef USE_VULKAN_API

#include <ATen/native/vulkan/api/QueryPool.h>

namespace at {
namespace native {
namespace vulkan {
namespace api {

class OpProfiler final {
 public:
  explicit OpProfiler(VkCommandBuffer buffer, QueryPool& querypool, const std::string& query_name)
    : buffer_(buffer),
      querypool_(querypool) {
    query_index_ = querypool.begin(buffer_, query_name);
  }
  OpProfiler(const OpProfiler&) = delete;
  OpProfiler(OpProfiler&&) = delete;
  OpProfiler& operator=(const OpProfiler&) = delete;
  OpProfiler& operator=(OpProfiler&&) = delete;
  ~OpProfiler() {
    querypool_.end(buffer_, query_index_);
  }

private:
  VkCommandBuffer buffer_;
  QueryPool& querypool_;
  int query_index_;
};

} // namespace api
} // namespace vulkan
} // namespace native
} // namespace at

#endif /* USE_VULKAN_API */
